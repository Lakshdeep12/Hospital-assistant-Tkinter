import tkinter as tk
from tkinter import messagebox, font, RIDGE, TOP, X, LEFT, RIGHT, BOTTOM
from PIL import Image, ImageTk
from datetime import datetime

def submit_form():
    messagebox.showinfo("Info", "LOGIN SUCCESSFULLY!")


root = tk.Tk()
root.title("JIET'X ONE CLINIC")
root.geometry("1540x750+0+0")
root.configure(bg="#1C2833")
# Title Label
lb1title = tk.Label(root, bd=20, relief=RIDGE, text="JIET'X ONE CLINIC", fg="#1C2833", bg="lightblue", font=("Comic Sans MS", 30, "bold"))
lb1title.pack(side=TOP, fill=X)

time_label = tk.Label( lb1title, font=("Comic Sans MS", 18), bg="lightblue", fg="#1C2833")
time_label.pack(side=tk.TOP, pady=(10, 10),anchor="e")

def update_time():
    """Update the time label with the current time."""
    current_time = datetime.now().strftime("%H:%M:%S")    
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  

update_time()




frame = tk.Frame(root, bg="#71797E", padx=45, pady=15, relief=tk.RAISED, borderwidth=5)
frame.place(relx=0.1, rely=0.2, anchor='nw')


box_font = font.Font(family="Georgia", size=16, weight="bold")
box_label = tk.Label(frame, text="Registration Here ", font=box_font, bg="white")
box_label.grid(row=0, column=0, columnspan=1, pady=(10, 10))


user_type = tk.StringVar(value="Patient")
patient_radio = tk.Radiobutton(frame, text="Patient Login", variable=user_type, value="Patient", bg="#2E86C1", font=("Comic Sans MS", 12))
doctor_radio = tk.Radiobutton(frame, text="Doctor Login", variable=user_type, value="Doctor", bg="#2E86C1", font=("Comic Sans MS", 12))


patient_radio.grid(row=1, column=0, padx=(0, 50), pady=(10, 10))
doctor_radio.grid(row=1, column=1, pady=(10, 10))


fields = [
    ("Full Username:", 2),
    ("Password:", 3),
    ("Date of Birth (YYYY-MM-DD):", 4),
    ("email:",5)
]

for label_text, row in fields:
    label = tk.Label(frame, text=label_text, bg="#ECF0F1", font=("Comic Sans MS", 12))
    label.grid(row=row, column=0, sticky='e', pady=(5, 5))
    entry = tk.Entry(frame, width=30)
    entry.grid(row=row, column=1, pady=(5, 5))

specialization_label = tk.Label(frame, text="Specialization:", bg="#ECF0F1", font=("Comic Sans MS", 12))
specialization_entry = tk.Entry(frame, width=30)

md_id_label = tk.Label(frame, text="MD ID:", bg="#ECF0F1", font=("Comic Sans MS", 12))
md_id_entry = tk.Entry(frame, width=30)

def toggle_fields():
    if user_type.get() == "Doctor":
        specialization_label.grid(row=2, column=2, sticky='e', padx=(10, 0), pady=(3, 3)) 
        specialization_entry.grid(row=2, column=3, padx=(10, 0), pady=(3, 3))  
        md_id_label.grid(row=3, column=2, sticky='e', padx=(10, 0), pady=(3, 3)) 
        md_id_entry.grid(row=3, column=3, padx=(10, 0), pady=(3, 3))  
    else:
        specialization_label.grid_forget()
        specialization_entry.grid_forget()
        md_id_label.grid_forget()
        md_id_entry.grid_forget()


patient_radio.config(command=toggle_fields)
doctor_radio.config(command=toggle_fields)


submit_button = tk.Button(frame, text="Submit", command=submit_form, bg="#2E86C1", font=("Comic Sans MS", 12), width=15, height=2)  
submit_button.grid(row=10, column=0, columnspan=2, pady=(20, 20))



image_path = r"C:\Users\HP\OneDrive\Desktop\chatbot\images hospital\hos.png" 
image = Image.open(image_path) 
photo = ImageTk.PhotoImage(image)


image_label = tk.Label(image=photo, borderwidth=5, relief="solid", bg="#1C2833")   
image_label.pack(side=tk.RIGHT, padx=(10,30), pady=(10,10))

root.mainloop()