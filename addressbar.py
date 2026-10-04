import ipaddress
import re
import webbrowser
from urllib.parse import urlencode, urlsplit


def resolve_address(address):
    """Return a web URL for an address-bar entry or a search query."""
    value = address.strip()
    if not value:
        raise ValueError("Lütfen bir adres veya arama terimi girin.")

    if re.search(r"\s", value):
        return _search_url(value)

    if re.match(r"^https?://", value, re.IGNORECASE):
        parsed = urlsplit(value)
        if not parsed.hostname:
            raise ValueError("Geçerli bir web adresi girin.")
        try:
            parsed.port
        except ValueError as error:
            raise ValueError("Web adresindeki bağlantı noktası geçersiz.") from error
        return value

    if re.match(r"^[a-z][a-z0-9+.-]*:", value, re.IGNORECASE) and not re.match(
        r"^[^/:?#]+:\d+(?:[/?#].*)?$", value
    ):
        raise ValueError("Yalnızca HTTP ve HTTPS adresleri desteklenir.")

    parsed = urlsplit(f"https://{value}")
    if not parsed.hostname:
        return _search_url(value)
    try:
        port = parsed.port
    except ValueError:
        return _search_url(value)

    hostname = parsed.hostname
    try:
        ipaddress.ip_address(hostname)
        is_ip_address = True
    except ValueError:
        is_ip_address = False

    if hostname == "localhost" or "." in hostname or is_ip_address or port is not None:
        return f"https://{value}"
    return _search_url(value)


def _search_url(query):
    return f"https://duckduckgo.com/?{urlencode({'q': query})}"


def main():
    import tkinter as tk
    from tkinter import ttk

    window = tk.Tk()
    window.title("Adres Çubuğu")
    window.geometry("640x120")
    window.minsize(420, 120)
    window.columnconfigure(0, weight=1)

    address = tk.StringVar()
    status = tk.StringVar(value="Bir web adresi veya arama terimi yazın.")

    entry = ttk.Entry(window, textvariable=address, font=("Sans", 15))
    entry.grid(row=0, column=0, sticky="ew", padx=(16, 8), pady=(20, 10))

    def open_address(_event=None):
        try:
            url = resolve_address(address.get())
        except ValueError as error:
            status.set(str(error))
            return

        try:
            opened = webbrowser.open_new_tab(url)
        except (OSError, webbrowser.Error):
            opened = False
        status.set(
            "Adres varsayılan tarayıcıda açıldı."
            if opened
            else "Tarayıcı açılamadı. Varsayılan tarayıcı ayarını kontrol edin."
        )

    button = ttk.Button(window, text="Git", command=open_address)
    button.grid(row=0, column=1, padx=(0, 16), pady=(20, 10))
    button.bind("<Return>", open_address)
    entry.bind("<Return>", open_address)

    ttk.Label(window, textvariable=status).grid(
        row=1, column=0, columnspan=2, sticky="w", padx=16, pady=(0, 12)
    )

    entry.focus_set()
    window.mainloop()


if __name__ == "__main__":
    main()
