# 🎙️ Voice Translator

**Voice Translator** is a Python desktop application that lets you speak in English and instantly get a Hindi translation. It uses **Google Speech Recognition** for speech-to-text and **Hugging Face Transformers (MarianMT)** for high-quality machine translation, all packed in a user-friendly **Tkinter GUI**.

---

## 🚀 Features

- 🎤 Record your voice in English  
- ✍️ See the real-time transcribed text  
- 🌐 Translates instantly from English ➡️ Hindi  
- 🖥️ Clean and responsive desktop interface  
- 🧠 Uses pre-trained NLP models for accurate translation  

---

## 📦 Requirements

- Python 3.7+
- pip

---

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/vatsala205/voice-translator.git
cd voice-translator
```
### Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt

```
### 🧪 How to Run
```bash
python main.py
```

### 🧠 How It Works
- Records your voice using speech_recognition
- Converts voice to text using Google's Speech API
- Translates English text to Hindi using Hugging Face MarianMT
- Displays results in a GUI made with Tkinter

### 🌍 Change Target Language
```python
src_lang = 'en'
tgt_lang = 'fr'  # Or 'de', 'es', etc.
```



