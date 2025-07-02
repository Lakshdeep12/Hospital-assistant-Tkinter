from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
import google.generativeai as genai
import pyttsx3
# Load API Key
load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")

if not genai_api_key:
    messagebox.showerror("Error", "API key not found. Please set the GOOGLE_API_KEY environment variable.")
    exit()
else:
    genai.configure(api_key=genai_api_key)

# Get Gemini response
def get_gemini_response(question):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Triggered when "Ask" button is pressed
def ask_question():
    question = entry.get()
    if not question.strip():
        messagebox.showwarning("Warning", "Please enter a question.")
        return
    response = get_gemini_response(question)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, response)
    # pyttsx3.speak(output_text)

# --- GUI Window Setup ---
root = tk.Tk()
root.title("LAKSHDEEP MEDICAL HEALTH CARE")
root.geometry("850x550")
root.configure(bg="#1B2631")

# Title Label
title_label = tk.Label(
    root,
    text="LAKSHDEEP MEDICAL HEALTH CARE",
    font=("Comic Sans MS", 22, "bold"),
    bg="lightblue",
    fg="#1B2631",
    pady=12,
    relief=tk.RAISED,
    borderwidth=4
)
title_label.pack(fill=tk.X, padx=20, pady=(15, 10))

# Main Frame (with black border look)
frame = tk.Frame(root, bg="#5D6D7E", padx=25, pady=25, bd=5, relief=tk.GROOVE, highlightbackground="black", highlightthickness=3)
frame.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

# Query Label
label = tk.Label(
    frame,
    text="Ask your medical query below:",
    font=("Comic Sans MS", 14, "bold"),
    bg="#5D6D7E",
    fg="white"
)
label.pack(pady=(0, 10))

# Entry field
entry = tk.Entry(frame, width=80, font=("Arial", 12), relief=tk.SUNKEN, bd=2)
entry.pack(pady=5)

# Ask Button
ask_button = tk.Button(
    frame,
    text="ASK THE QUERY",
    command=ask_question,
    font=("Comic Sans MS", 12, "bold"),
    bg="black",
    fg="white",
    padx=10,
    pady=6,
    relief=tk.RAISED,
    bd=3
)
ask_button.pack(pady=6, anchor='s')  # aligned to right

# Output Display
output_text = scrolledtext.ScrolledText(
    frame,
    wrap=tk.WORD,
    width=90,
    height=12,
    font=("Arial", 11),
    relief=tk.SUNKEN,
    bd=3,
    bg="#FDFEFE"
)
output_text.pack(pady=(5, 0))

root.mainloop()
