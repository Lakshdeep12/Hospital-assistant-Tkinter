from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess 
import os
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

MainFrame = Frame(root, bd=16, relief=RIDGE, bg="#34495E")
MainFrame.place(x=6, y=100, width=1270, height=580)

# Left Frame
DataFrameLeft = LabelFrame(
    MainFrame,
    bd=10,
    relief=RIDGE,
    padx=10,
    font=("Times New Roman", 20, "bold"),
    text="Welcome Dr. Gulati",
    bg="#34495E",
    fg="white"
)
DataFrameLeft.place(x=10, y=10, width=760, height=530)

# Frame to hold image and fields side-by-side
content_frame = Frame(DataFrameLeft, bg="#34495E")
content_frame.place(x=10, y=10)

# Load and display photo (left side)
try:
    image_path = r"C:\Users\HP\OneDrive\Desktop\chatbot\images hospital\doctor.png"
    image = Image.open(image_path)
    image = image.resize((250, 220))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(content_frame, image=photo, bg="#34495E")
    image_label.image = photo
    image_label.grid(row=0, column=0, padx=10, pady=10, sticky=N)
except Exception as e:
    print("Image load error:", e)

# Frame for doctor info (right side of content_frame)
info_frame = Frame(content_frame, bg="#34495E")
info_frame.grid(row=0, column=1, padx=20, pady=10, sticky=N)

# Doctor Info Labels and Values (fixed labels, no entry boxes)
doctor_info = {
    "Doctor Name:": "Dr. Mashur Gulati",
    "Age:": "47",
    "Specialization:": "Physician",
    "Attendance:": "100%",
    "Phone Number:": "9462744883",
    "Education:": "MBBS",
    "Surgery Perform:": "21"
}

for i, (label, value) in enumerate(doctor_info.items()):
    lbl = Label(info_frame, text=label, bg="#34495E", fg="white", font=("Comic Sans MS", 12, "bold"))
    lbl.grid(row=i, column=0, sticky=W, padx=5, pady=5)
    val_lbl = Label(info_frame, text=value, bg="#34495E", fg="white", font=("Comic Sans MS", 12))
    val_lbl.grid(row=i, column=1, sticky=W, padx=5, pady=5)

# Frame for buttons (at the bottom, full width of left frame)
button_frame = Frame(DataFrameLeft, bg="#34495E")
button_frame.place(relx=0.5, rely=1.0, anchor='s', width=740, height=50)

# Button style
btn_style = {
    "width": 15,
    "padx": 2,
    "pady": 2,
    "bg": "lightblue",
    "fg": "#1C2833",
    "font": ("Comic Sans MS", 12, "bold"),
    "relief": "raised",
    "bd": 3
}

# Button actions
def open_certificate():
    subprocess.Popen(["python", "certificate.py"])

def open_chatbot():
    subprocess.Popen(["python", r"medical bot\app.py"])

def manage_patient():
    subprocess.Popen(["python", r"C:\Users\HP\OneDrive\Desktop\chatbot\patient.py"])

def open_health_tip():

    health_tips_path = r"C:\Users\HP\OneDrive\Desktop\chatbot\heath tips.txt"   
    if os.path.exists(health_tips_path):
        os.startfile(health_tips_path)
    else:
        messagebox.showerror("Error", "Health tips file not found.")

def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        root.destroy()

# Create and pack buttons horizontally
buttons = [
    ("Chatbot", open_chatbot),
    ("Manage Patient", manage_patient),
    ("Open Certificate", open_certificate),
    ("Open Health Tip", open_health_tip),
    ("Logout", logout)
]

for idx, (text, command) in enumerate(buttons):
    btn = Button(button_frame, text=text, command=command, **btn_style)
    btn.grid(row=0, column=idx, padx=5, pady=5, sticky='ew')

# Configure equal weight for all button columns to evenly space them
for idx in range(len(buttons)):
    button_frame.grid_columnconfigure(idx, weight=1)

# Right Frame
DataFrameRight = LabelFrame(
    MainFrame,
    bd=10,
    relief=RIDGE,
    padx=10,
    font=("Times New Roman", 18, "bold"),
    text="Your Info",
    bg="#34495E",
    fg="white"
)
DataFrameRight.place(x=780, y=10, width=450, height=535)

# Scrollbar and Text Widget
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
about_us_info =  '''I am Dr. Mashur Gulati, a board-certified family medicine physician with 12 years of experience caring for patients of all ages. I graduated from Johns Hopkins University School of Medicine and completed my residency at Massachusetts General Hospital. I specialize in preventive care, chronic disease management, and women's health at Community Health Center. 

I am fluent in both English and Spanish, which allows me to better serve my diverse patient community. I believe in building strong relationships with my patients and taking a collaborative approach to healthcare.

My practice philosophy centers on treating the whole person, not just symptoms, and I work closely with each patient to develop personalized treatment plans that fit their lifestyle and goals.

I stay current with the latest medical research and regularly attend continuing education conferences to ensure I'm providing the most effective care.

\n\n— by Lakshdeep Singh'''

about_text.insert(END, about_us_info)
about_text.config(state=DISABLED)

# Run main loop
root.mainloop()

