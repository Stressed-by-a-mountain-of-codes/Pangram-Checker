import tkinter as tk
from tkinter import messagebox
import string
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_pangram(event=None):
    text = entry.get().lower()
    if not text.strip():
        messagebox.showerror("Input Error", "Please enter a sentence.")
        return

    all_letters = set(string.ascii_lowercase)
    present = set(c for c in text if c in all_letters)
    missing = sorted(all_letters - present)

    is_pangram = len(missing) == 0

    if is_pangram:
        result_label.config(text="✅ Pangram: All 26 letters present!", fg="green")
        speak("Yes, it is a pangram.")
    else:
        result_label.config(
            text=f"❌ Not a Pangram. Missing: {', '.join(missing)}", fg="red"
        )
        speak("No, it's not a pangram.")

    show_alphabet_coverage(present, missing)
    root.after(3000, reset)

def show_alphabet_coverage(present, missing):
    text_box.delete("1.0", tk.END)
    for letter in string.ascii_lowercase:
        if letter in present:
            text_box.insert(tk.END, letter.upper() + " ", "green")
        else:
            text_box.insert(tk.END, letter.upper() + " ", "red")

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")
    text_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Pangram Checker with Missing Letters & Voice")
root.geometry("520x300")
root.resizable(False, False)

tk.Label(root, text="Enter a sentence:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center", width=46)
entry.pack(pady=5)
entry.bind("<Return>", check_pangram)

tk.Button(root, text="Check Pangram", font=("Arial", 12), command=check_pangram).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

text_box = tk.Text(root, height=2, width=45, font=("Courier", 14), wrap="none", bd=0)
text_box.tag_config("green", foreground="green")
text_box.tag_config("red", foreground="red")
text_box.pack(pady=5)

entry.focus()
root.mainloop()
