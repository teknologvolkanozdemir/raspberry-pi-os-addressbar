# Raspberry Pi OS Adres Çubuğu

Python ve Tkinter ile hazırlanmış küçük bir adres çubuğu. Girilen web adreslerini
Raspberry Pi OS üzerindeki varsayılan tarayıcıda açar; adres olmayan metinleri
DuckDuckGo'da arar.

## Gereksinimler

- Python 3
- Tkinter (`python3-tk`)
- Raspberry Pi OS'te yapılandırılmış varsayılan bir web tarayıcısı

Tkinter kurulu değilse terminalde yükleyin:

```sh
sudo apt update
sudo apt install python3-tk
```

## Çalıştırma

Depo dizininde terminal açıp şu komutu çalıştırın:

```sh
python3 addressbar.py
```

Adres çubuğuna `https://example.com` veya `example.com` yazın. Bir arama
terimi girerseniz DuckDuckGo sonuçları varsayılan tarayıcıda açılır. Adresi
Enter tuşuyla veya **Git** düğmesiyle gönderebilirsiniz.

## Testler

```sh
python3 -m unittest
```
