# Raspberry Pi OS Adres Çubuğu

Raspberry Pi OS üzerinde çalışan basit bir adres çubuğu. Web adreslerini
sistemin varsayılan tarayıcısında açar; adres olmayan metinleri Google'da arar.

## Kurulum ve kullanım

```sh
sudo apt update
sudo apt install python3-tk
python3 addressbar.py
```

Bir adresi veya arama metnini yazıp **Enter** tuşuna basın. `example.com`
gibi adresler HTTPS ile açılır; `localhost:8000` HTTP kullanır. `Ctrl+L`
adres alanına odaklanır.

## Testler

```sh
python3 -m unittest discover -s tests
```
