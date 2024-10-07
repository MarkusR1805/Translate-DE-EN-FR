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

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
