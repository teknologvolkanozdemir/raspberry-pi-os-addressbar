#!/usr/bin/env python3
"""Raspberry Pi OS için basit web tarayıcısı (adres çubuğu + gezinme düğmeleri)."""
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QLineEdit, QMainWindow, QToolBar,
                             QStyle)
from PyQt5.QtWebEngineWidgets import QWebEngineView

HOME_URL = "https://www.google.com"
SEARCH_URL = "https://www.google.com/search?q="


def build_url(text):
    """Adres çubuğuna yazılan metni URL'ye veya arama sorgusuna çevirir."""
    text = text.strip()
    if not text:
        return QUrl(HOME_URL)
    if "://" in text:
        return QUrl(text)
    if " " not in text and ("." in text or text.startswith("localhost")):
        return QUrl("https://" + text)
    return QUrl(SEARCH_URL + QUrl.toPercentEncoding(text).data().decode())


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pi Tarayıcı")
        self.resize(1024, 700)

        self.view = QWebEngineView()
        self.setCentralWidget(self.view)

        bar = QToolBar("Gezinme")
        self.addToolBar(bar)
        style = self.style()
        for icon, tip, slot in (
            (QStyle.SP_ArrowBack, "Geri", self.view.back),
            (QStyle.SP_ArrowForward, "İleri", self.view.forward),
            (QStyle.SP_BrowserReload, "Yenile", self.view.reload),
            (QStyle.SP_DirHomeIcon, "Ana sayfa", self.go_home),
        ):
            act = bar.addAction(style.standardIcon(icon), tip)
            act.triggered.connect(slot)

        self.address = QLineEdit()
        self.address.setPlaceholderText("Adres yazın veya arayın")
        self.address.returnPressed.connect(self.navigate)
        bar.addWidget(self.address)

        self.view.urlChanged.connect(
            lambda u: self.address.setText(u.toString()))
        self.view.titleChanged.connect(
            lambda t: self.setWindowTitle(f"{t} - Pi Tarayıcı"))
        self.go_home()

    def go_home(self):
        self.view.setUrl(QUrl(HOME_URL))

    def navigate(self):
        self.view.setUrl(build_url(self.address.text()))


def main():
    app = QApplication(sys.argv)
    win = Browser()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
