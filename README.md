Sure! Here's a clean and professional `README.md` for your project that fits GitHub style and your app’s description:

---

```markdown
# English to Darija Translator 🇬🇧➡️🇲🇦

A simple yet clever web-based **English to Darija (Moroccan Arabic)** translator built with Flask.

## 🧠 How it Works

- Uses a large dataset of English–Darija phrase pairs stored in `dataset.csv`.
- Translates full sentences or phrases using a combination of:
  - Phrase matching
  - Word-by-word translation
  - Text correction via `TextBlob`
- Learns over time — users can add new phrase pairs through the interface.

## 🖥️ Features

- Translate English sentences into Darija.
- Add your own phrases to the dataset.
- Intelligent matching for multi-word phrases.
- Auto-correction for better translation accuracy.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure you also download NLTK's tokenizer data:

```python
import nltk
nltk.download('punkt')
```

### 3. Run the app

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000`.

## 🗃️ Dataset

The translator uses a CSV dataset (`dataset.csv`) where each row is a pair:
```
darija,english
```
Example:
```
labas 3lik,how are you
```

## 📁 File Structure

```
├── app.py                  # Main Flask app
├── last.py                 # Core translation logic and helper functions
├── dataset.csv             # Translation data
├── templates/
│   └── try.html            # HTML interface
```

## 📅 Project Info

- **Created:** April 2024
- **Made with ❤️ by HIM7**

---

Feel free to contribute or suggest improvements!
```

---

Let me know if you'd like to include screenshots or deployment steps too!
