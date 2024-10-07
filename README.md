# Translate Deutsch-Englisch-Französisch
## Modelle von Helsinki-NLP von Hugging Faces
***
[![N|Solid](https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/9c0923a3-46bb-4a4d-be73-66e72d7a4c4c/original=true,quality=90/11945886.jpeg)](https://civitai.com/user/Der_Zerfleischer)
***
Übersetzen von Deutsch auf Englisch und Französisch aber auch umgekehrt
Verwendet werden die Open-Source-Modelle von Helsinki-NLP die man auch lokal installieren kann und somit unabhängig von einer Onlineverbindung ist.

## Für wen geeignet
- Ideal für Schüler
-- Zum lernen und zum überprüfen von gelerntem
-- Um Texte aus dem Internet schnell und einfach zu übersetzen (je nach Kontext, eine 100%ige Garantie kann ich nicht zusichern)
- Für Anwender wie mich die sich auf vielen Inhalten in Englisch rumschlagen müssen ;-)
***
## Warum dieses Programm

- Keine teuren Abo's von irgendwelchen Clouddiensten, Chatbots usw.
- Wenn man die Modelle nicht lokal verwendet benötigt man kaum Speicherplatz, ideal für gelegentliche Anwendung
- Durch lokale Installation der Modelle unabhängig vom Anbieter der Modelle (Hugging Face), ideal wenn man sehr oft dieses Programm anwendet (Speicherplatz ca. 4GB)
- Für PC/MAC ab 8GB Arbeitsspeicher

# Einfache Umstellung auf lokale Installation
Diesen Quellcode:

> Laden der Modelle deutsch / englisch und umgekehrt
> de_to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-de-en", device=device)
> en_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de", device=device)
> Laden der Modelle französisch / deutsch und umgekehrt
> de_to_fr = pipeline("translation", model="Helsinki-NLP/opus-mt-de-fr", device=device)
> fr_to_de = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-de", device=device)

in diesen umändern (den Pfad anpassen)

> Laden der Modelle deutsch / englisch und umgekehrt
> de_to_en = pipeline("translation", model="Helsinki-NLP-opus-mt-de-en", device=device)
> en_to_de = pipeline("translation", model="Helsinki-NLP-opus-mt-en-de", device=device)
> Laden der Modelle französisch / deutsch und umgekehrt
> de_to_fr = pipeline("translation", model="Helsinki-NLP-opus-mt-de-fr", device=device)
> fr_to_de = pipeline("translation", model="Helsinki-NLP-opus-mt-fr-de", device=device)

## 100%ige Garantie der korrekten Übersetzen

Wie mit allen KI-Modellen kann man keine 100%ige Garantie geben ob der Text korrekt übersetzt wird, auch ich übernehme keine Haftung

```sh
pip install gradio
pip install transformers
pip install torch
```
oder
```sh
pip install --upgrade gradio
pip install --upgrade transformers
pip install --upgrade torch
```

## Python 3.10, 3.11 oder 3.12
Python sollte installiert sein!

## Installation von Python

[Python 3.12 für Windows 64bit](https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe)
### Bei Windows unbedingt das Häckchen setzen "Pfad hinzufügen"
[Python 3.12 für Mac M1,M2,M3](https://www.python.org/ftp/python/3.12.7/python-3.12.7-macos11.pkg)

### Start des Programmes aus dem Verzeichnis in dem das Programm installiert wurde
```sh
python main.py
```
## Ein Video zur Installation auf dem Mac folgt und der Link wird demnächst hier verlinkt!