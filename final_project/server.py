from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.english_to_french(textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return machinetranslation.french_to_english(textToTranslate)


@app.route("/")
def index():
    return render_template('index.html')


def renderIndexPage():
    # Write the code to render template
    print()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
