from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

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
    text="Welcome Mr. Lavanya",
    bg="#34495E",
    fg="white"
)
DataFrameLeft.place(x=10, y=10, width=760, height=530)

# Frame to hold image and patient info side-by-side
content_frame = Frame(DataFrameLeft, bg="#34495E")
content_frame.place(x=10, y=10)

# Load and display patient photo (left side)
try:
    image_path = r"C:\Users\HP\OneDrive\Desktop\chatbot\images hospital\download (5).png"  # Update with the correct path
    image = Image.open(image_path)
    image = image.resize((130, 160))
    photo = ImageTk.PhotoImage(image)
    image_label = Label(content_frame, image=photo, bg="#34495E")
    image_label.image = photo
    image_label.grid(row=0, column=0, padx=5, pady=10, sticky=N)
except Exception as e:
    print("Image load error:", e)

# Frame for patient info (right side of content_frame)
info_frame = Frame(content_frame, bg="#34495E")
info_frame.grid(row=0, column=1, padx=20, pady=10, sticky=N)

# Patient Info Labels and Values (fixed labels, no entry boxes)
patient_info = {
    "Name:": "Lavanya Gehlot",
    "Patient ID:": "P123456",
    "Age:": "45",
    "Gender:": "Female",
    "Blood Group:": "B+",
    "Contact Number:": "+91-9876543210",
    "Address:": "12, MG Road, Bengaluru, Karnataka",
    "Current Medications:": "Metformin 500mg, Amlodipine 5mg",
    "Upcoming Appointment:": "10th June 2025, 11:00 AM with Dr. Meena (Psychiatrist)",
    "Last Test Result:": "Blood Sugar (Fasting): 110 mg/dL – Normal"
}

for i, (label, value) in enumerate(patient_info.items()):
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
def open_chatbot():
    messagebox.showinfo("Chatbot", "Chatbot feature coming soon.")

def open_certificate():
    messagebox.showinfo("Certificate", "Open Certificate feature coming soon.")

def open_health_tip():
    messagebox.showinfo("Health Tip", "Open Health Tip feature coming soon.")

def logout():
    if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
        root.destroy()

# Create and pack buttons horizontally
buttons = [
    ("Chatbot", open_chatbot),
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

# Configure scrollbar to work with the text widget
about_scrollbar.config(command=about_text.yview)

# About Us Content
about_us_info =  '''Patient: Lavanya
Condition: Chronic Constipation
Treatment Period: 3 Months
Ms. Lavanya presented with chronic constipation characterized by infrequent bowel movements, abdominal discomfort, and straining during defecation. Initial assessment revealed decreased bowel movement frequency (2-3 times per week) and hard, difficult-to-pass stools.. Regular follow-ups monitored treatment response and medication adjustments.
After three months of consistent treatment, Ms. Lavanya demonstrated significant improvement with regular daily bowel movements, reduced straining, and improved stool consistency. Patient reported enhanced quality of life and digestive comfort. Maintenance therapy with dietary modifications and occasional fiber supplementation was recommended for sustained results. Complete resolution of constipation symptoms achieved successfully.'''

about_text.insert(END, about_us_info)
about_text.config(state=DISABLED)

# Run main loop
root.mainloop()
