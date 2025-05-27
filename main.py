import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from transformers import MarianMTModel, MarianTokenizer
import torch

# Set source and target languages
src_lang = 'en'
tgt_lang = 'hi'  # You can change this to any MarianMT-supported language code

# Load model & tokenizer
model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Speech recognizer
recognizer = sr.Recognizer()

def record_and_translate():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...", fg="blue")
            window.update()
            audio = recognizer.listen(source, timeout=5)
            status_label.config(text="Processing...", fg="orange")
            window.update()
            text = recognizer.recognize_google(audio)
            original_text.delete(1.0, tk.END)
            original_text.insert(tk.END, text)

            # Translation
            inputs = tokenizer(text, return_tensors="pt", padding=True)
            translated = model.generate(**inputs)
            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, translated_text)
            status_label.config(text="Done", fg="green")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error", fg="red")

# UI setup
window = tk.Tk()
window.title("Voice Translator")
window.geometry("500x400")
window.config(bg="#f2f2f2")

title_label = tk.Label(window, text="Voice Translator", font=("Helvetica", 20, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

record_btn = tk.Button(window, text="Record Voice", command=record_and_translate, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
record_btn.pack(pady=10)

status_label = tk.Label(window, text="", font=("Helvetica", 10), bg="#f2f2f2")
status_label.pack()

tk.Label(window, text="Original Text:", bg="#f2f2f2").pack()
original_text = tk.Text(window, height=5, width=60)
original_text.pack(pady=5)

tk.Label(window, text="Translated Text:", bg="#f2f2f2").pack()
output_text = tk.Text(window, height=5, width=60)
output_text.pack(pady=5)

window.mainloop()
