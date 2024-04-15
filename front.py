from flask import Flask, render_template, request
from last import app, translate, load_translation_dict, add_phrase_to_dict  # Importez app depuis last.py

app = Flask(__name__)

# Import functions from last.py after defining app
from last import translate, load_translation_dict  

@app.route('/')
def translator():
    return render_template('try.html')  # Change this line

@app.route('/try.html')
def home():
    return render_template('try.html')

@app.route("/translate", methods=["POST"])
def translate_text():
    if request.method == "POST":
        input_text = request.form['english-input']
        print("Input Text:", input_text)
        output = translate(input_text, translation_dict)
        return render_template('try.html', output=output, input_text=input_text)
    

@app.route("/add_phrase", methods=["GET", "POST"])
def add_phrase():
    if request.method == "POST":
        english_phrase = request.form['english-phrase']
        darija_phrase = request.form['darija-phrase']
        add_phrase_to_dict(english_phrase, darija_phrase, 'dataset.csv')  # Ajoutez la phrase à votre dictionnaire de traduction
        return render_template('try.html')

if __name__ == '__main__':
    # Load the translation dictionary
    translation_dict = load_translation_dict('dataset.csv')
    app.run(debug=True)
