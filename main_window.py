from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess  
from PIL import Image, ImageTk
from datetime import datetime

current_datetime = datetime.now().strftime("%d-%m-%Y  %I:%M %p")

def open_login():
    subprocess.Popen(["python", "authentication.py"])

def open_register():
    subprocess.Popen(["python", "registration.py"])

def open_doctor_dashboard():
    subprocess.Popen(["python", "doctor_dashboard.py"])

def open_patient_dashboard():
    subprocess.Popen(["python", "patient_dashboard.py"])

def open_certificate():
    subprocess.Popen(["python", "certificate.py"])

def open_chatbot():
    subprocess.Popen(["python", r"medical bot\app.py"])

import os

tip_index = [0]
health_tips = []

def load_health_tips():
    try:
        with open(r"C:\Users\HP\OneDrive\Desktop\chatbot\heath tips.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            tips = [line.strip() for line in lines if line.strip()]
            
            return tips
    except FileNotFoundError:
        print("Health tips file not found.")
        return ["Health tips file not found."]
    except Exception as e:
        print("Error reading health tips:", e)
        return ["Error loading health tips."]

def show_next_tip():
    if not health_tips:
        return
    tip_index[0] = (tip_index[0] + 1) % len(health_tips)
    print("Displaying tip:", health_tips[tip_index[0]])  # Debug output
    tip_label.config(text=health_tips[tip_index[0]])
    tip_label.update()

# Load the tips once at startup
health_tips = load_health_tips()

# Create the main window
root = Tk()
root.title("JIET'X ONE CLINIC")
root.geometry("1540x750+0+0")
root.configure(bg="#1C2833")

# Title Label
lb1title = Label(
    root,
    bd=20,
    relief=RIDGE,
    text="JIET'X ONE CLINIC",
    fg="#1C2833",
    bg="lightblue",
    font=("Comic Sans MS", 30, "bold")
)
lb1title.pack(side=TOP, fill=X)

HealthTipFrame = Frame(root, bd=6, relief=RIDGE, bg="lightblue")
HealthTipFrame.pack(fill=X)

tip_label = Label(
    HealthTipFrame,
    text=health_tips[0] if health_tips else "No tips available.",
    font=("Comic Sans MS", 12, "italic"),
    fg="#1C2833",
    bg="lightblue",
    anchor="w"
)
tip_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")

# Login and Register buttons
tip_btn_style = {
    "bg": "#1C2833",
    "fg": "white",
    "font": ("Comic Sans MS", 10, "bold"),
    "width": 12
}

login_btn = Button(HealthTipFrame, text="Login", command=open_login, **tip_btn_style)
login_btn.grid(row=0, column=2, padx=10)

register_btn = Button(HealthTipFrame, text="Register", command=open_register, **tip_btn_style)
register_btn.grid(row=0, column=3, padx=10)

# Next Tip Button
next_tip_btn = Button(
    HealthTipFrame,
    text="Next Tip",
    command=show_next_tip,
    bg="#2980B9",
    fg="white",
    font=("Comic Sans MS", 10, "bold"),
    width=12
)
next_tip_btn.grid(row=0, column=1, padx=20, sticky="e")
datetime_label = Label(
    HealthTipFrame,
    text=current_datetime,
    font=("Comic Sans MS", 10, "bold"),
    fg="#1C2833",
    bg="lightblue"
)
datetime_label.grid(row=0, column=5, padx=10)


def auto_rotate_tips():
    if not health_tips:
        return
    tip_index[0] = (tip_index[0] + 1) % len(health_tips)
    tip_label.config(text=health_tips[tip_index[0]])
    tip_label.update()
    root.after(7000, auto_rotate_tips)  # Call this function again after 7000 ms (7 sec)

# Load the tips once at startup
health_tips = load_health_tips()
auto_rotate_tips()  # Start auto-rotation

# Main Frame
MainFrame = Frame(root, bd=16, relief=RIDGE, bg="#34495E")
MainFrame.place(x=10, y=150, width=1265, height=500)
# Footer inside the MainFrame
FooterFrame = Frame(MainFrame, bg="lightblue", bd=5, relief=RIDGE)
FooterFrame.place(x=10, y=440, width=1220, height=25)

footer_text = Label(
    FooterFrame,
    text="LinkedIn: Lakshdeep Singh    |    Instagram: lakshdeep_solanki_12    |    Phone: 9257159368",
    font=("Comic Sans MS", 10, "bold"),
    bg="lightblue",
    fg="#1C2833",
    anchor="center"
)
footer_text.pack(fill=BOTH, expand=True)

# Left Frame
DataFrameLeft = LabelFrame(
    MainFrame,
    bd=10,
    relief=RIDGE,
    padx=10,
    font=("Times New Roman", 20, "bold"),
    text="Welcome to JIET'X",
    bg="#34495E",
    fg="white"
)
DataFrameLeft.place(x=10, y=10, width=760, height=430)

# Buttons on the left side
btn_style = {
    "width": 25,
    "padx": 2,
    "pady": 2,
    "anchor": "w",
    "bg": "light blue",
    "fg": "#34495E",
    "font": ("Comic Sans MS", 12, "bold")
}

# Buttons on the left side
btn_style = {
    "width": 25,
    "padx": 3,
    "pady": 2,
    "bg": "light blue",
    "fg": "#34495E",
    "font": ("Comic Sans MS", 12, "bold")
}

Button(DataFrameLeft, text="Doctor's Dashboard", command=open_doctor_dashboard, **btn_style).pack(anchor="w", padx=20, pady=5)
Button(DataFrameLeft, text="Patient's Dashboard", command=open_patient_dashboard, **btn_style).pack(anchor="w", padx=20, pady=5)
Button(DataFrameLeft, text="Certificate", command=open_certificate, **btn_style).pack(anchor="w", padx=20, pady=5)
Button(DataFrameLeft, text="Chatbot", command=open_chatbot, **btn_style).pack(anchor="w", padx=20, pady=5)

# Load and display photo
try:
    image_path = r"C:\\Users\\HP\\OneDrive\\Desktop\\chatbot\\images hospital\\blackbox.png"
    image = Image.open(image_path)
    image = image.resize((350, 320))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(DataFrameLeft, image=photo, bg="#34495E")
    image_label.image = photo  # Keep a reference!
    # Place the image_label at top-right corner with some padding (30 px right, 5 px top)
    image_label.place(relx=1.0, rely=0.0, anchor='ne', x=-30, y=5)
except Exception as e:
    print("Image load error:", e)

DataFrameRight = LabelFrame(
    MainFrame,
    bd=10,
    relief=RIDGE,
    padx=10,
    font=("Times New Roman", 18, "bold"),
    text="About Us",
    bg="#34495E",
    fg="white"
)
DataFrameRight.place(x=780, y=10, width=450, height=430)

# Scrollbar and Text Widget for About Us
about_scrollbar = Scrollbar(DataFrameRight)
about_scrollbar.pack(side=RIGHT, fill=Y)

about_text = Text(
    DataFrameRight,
    wrap=WORD,
    font=("Comic Sans MS", 12),
    bg="#34495E",
    fg="white",
    yscrollcommand=about_scrollbar.set,
    relief=FLAT,
)
about_text.pack(fill=BOTH, expand=True)
about_scrollbar.config(command=about_text.yview)

# About Us Content
about_us_info = """We are a team of passionate developers dedicated to creating smart, efficient, and user-friendly healthcare solutions. 

Our Hospital Assistant System with AI Chat Support is designed to modernize the way hospitals and clinics manage patient care, streamline administrative tasks, and provide quick health-related assistance through intelligent automation.

With a focus on simplicity, accessibility, and innovation, our system offers essential modules such as patient and doctor management, billing, and a built-in AI chatbot.

Whether for small clinics or medium-scale hospitals, this solution is aimed at improving overall workflow, reducing manual effort, and enhancing patient experience through technology.

— by Lakshdeep Singh"""

about_text.insert(END, about_us_info)
about_text.config(state=DISABLED)  # make it read-only

# Start the main loop
root.mainloop()
