import re
import webbrowser
from urllib.parse import urlencode


def address_to_url(address):
    address = address.strip()
    if not address:
        return None

    if re.match(r"^https?://", address, re.IGNORECASE):
        return address

    if re.match(r"^localhost(?::\d+)?(?:/|$)", address, re.IGNORECASE):
        return f"http://{address}"

    host = address.split("/", 1)[0]
    if re.match(r"^www\.", address, re.IGNORECASE) or "." in host:
        return f"https://{address}"

    return f"https://www.google.com/search?{urlencode({'q': address})}"


def main():
    import tkinter as tk
    from tkinter import messagebox, ttk

    root = tk.Tk()
    root.title("Adres Çubuğu")
    root.geometry("520x100")
    root.minsize(320, 100)

    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Adres veya arama:").pack(anchor="w")

    address_entry = ttk.Entry(frame)
    address_entry.pack(fill="x", expand=True, pady=(6, 0))

    def open_address(event=None):
        url = address_to_url(address_entry.get())
        if url and not webbrowser.open_new_tab(url):
            messagebox.showerror(
                "Tarayıcı açılamadı",
                "Varsayılan web tarayıcısı açılamadı.",
                parent=root,
            )

    address_entry.bind("<Return>", open_address)
    root.bind("<Control-l>", lambda event: address_entry.focus_set())
    address_entry.focus_set()
    root.mainloop()


if __name__ == "__main__":
    main()
