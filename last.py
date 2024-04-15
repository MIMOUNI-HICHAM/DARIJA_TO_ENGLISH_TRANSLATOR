import csv
import string
import nltk
from collections import defaultdict
from flask import request, render_template
from flask import Flask
from textblob import Word

app = Flask(__name__)

def load_translation_dict(file_path):
    translation_dict = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if len(row) < 2:  # Skip rows with less than 2 values
                continue
            darija, english = row
            translation_dict[english.lower()].append(darija)
    return translation_dict

def translate(sentence, translation_dict):
    # Remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = nltk.word_tokenize(sentence.lower())
    translated_words = []
    i = 0
    while i < len(words):
        # Check phrases in the translation dictionary
        matches = []
        for j in range(i + len(words), i, -1):  # Check sequences of length len(words) to 1
            phrase = ' '.join(words[i:j])
            if phrase in translation_dict:
                matches.append((j-i, phrase))
        if matches:  # If matches were found
            # Sort matches by length in descending order and choose the longest
            matches.sort(key=lambda x: x[0], reverse=True)
            length, phrase = matches[0]
            translated_words.append(translation_dict[phrase][0])  # Select the first translation option
            i += length
        else:  # No match was found
            # Use TextBlob to correct the word
            corrected_word = Word(words[i]).correct()
            # If the corrected word is in the dictionary, translate it
            if corrected_word in translation_dict:
                translated_words.append(translation_dict[corrected_word][0])
            else:  # If the corrected word is still not in the dictionary, return the original word
                translated_words.append(words[i])
            i += 1
    return ' '.join([str(word) for word in translated_words])

def add_phrase_to_dict(english_phrase, darija_phrase, file_path):
    with open(file_path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([english_phrase, darija_phrase])
        
def add_phrase():
    if request.method == "POST":
        english_phrase = request.form['english-phrase']
        darija_phrase = request.form['darija-phrase']
        add_phrase_to_dict(english_phrase, darija_phrase, 'dataset.csv')
        # Reload the translation dictionary
        global translation_dict
        translation_dict = load_translation_dict('dataset.csv')
        return render_template('try.html')
