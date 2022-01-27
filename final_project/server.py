from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def en_to_fr(en_text):
    """
    #this function translate english to french
    """
    fr_tran = language_translator.translate(text=en_text, model_id='en-fr').get_result()

    return fr_tran['translations'][0]['translation']

@app.route("/frenchToEnglish")
def fr_to_en(fr_text):
    """
    #this function translate french to english
    """

    en_tran = language_translator.translate(text=fr_text, model_id='fr-en').get_result()

    return en_tran['translations'][0]['translation']

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
