import tkinter as tk
from tkinter import messagebox, font
from datetime import datetime

# Function to calculate total fees
def calculate_total():
    try:
        lab_test_charge = float(entries["lab_test_entry"].get())
        doctor_fees = float(entries["doctor_fees_entry"].get())
        nursing_fees = float(entries["nursing_fees_entry"].get())
        room_fees = float(entries["room_fees_entry"].get())
        medicine_fees = float(entries["medicine_fees_entry"].get())

        if admit_var.get() == "Yes":
            total_fees = lab_test_charge + doctor_fees + nursing_fees + room_fees + medicine_fees
        else:
            total_fees = lab_test_charge + doctor_fees + nursing_fees + medicine_fees

        total_fees_label.config(text=f"Total Fees: ₹ {total_fees:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for charges.")

# Initialize main window
root = tk.Tk()
root.title("HEALTH CARE HUB")
root.geometry("1000x720")
root.configure(bg="#1C2833")

# Clock
time_label = tk.Label(root, font=("Comic Sans MS", 18), bg="#1C2833", fg="white")
time_label.pack(side=tk.TOP, pady=(10, 5))

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

update_time()

# Title
title_font = font.Font(family="Comic Sans MS", size=30, weight="bold")
title_label = tk.Label(root, text="JIET'X ONE CLINIC", font=title_font, bg="lightblue", fg="#2C3E50", relief=tk.RAISED, borderwidth=3)
title_label.pack(pady=(5, 10))

# Main container frame with black border
outer_frame = tk.Frame(root, bg="black", padx=3, pady=3)
outer_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Inner frame
frame = tk.Frame(outer_frame, bg="#5D6D7E", padx=30, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Patient's Bill heading
box_font = font.Font(family="Comic Sans MS", size=18, weight="bold")
box_label = tk.Label(frame, text="PATIENT'S BILL", font=box_font, bg="white", width=25, relief=tk.RAISED, bd=2)
box_label.grid(row=0, column=0, columnspan=4, pady=(10, 20), padx=10)

# Patient form fields
fields = [
    ("Patient ID:", "patient_id_entry"),
    ("Patient Name:", "patient_name_entry"),
    ("Gender:", "gender_entry"),
    ("D.O.B:", "dob_entry"),
    ("Age:", "age_entry"),
    ("Phone Number:", "phone_entry"),
    ("Email:", "email_entry"),
    ("Blood Group:", "blood_group_entry"),
    ("Lab Test Charge:", "lab_test_entry"),
    ("Doctor Fees:", "doctor_fees_entry"),
    ("Nursing Staff Fees:", "nursing_fees_entry"),
    ("Room Fees:", "room_fees_entry"),
    ("Medicine Fees:", "medicine_fees_entry"),
]

entries = {}

# Create left and right side form layout
for i, (label_text, var_name) in enumerate(fields):
    column = 0 if i < 7 else 2
    row = i if i < 7 else i - 7

    label = tk.Label(frame, text=label_text, bg="#5D6D7E", fg="white", font=("Comic Sans MS", 12))
    label.grid(row=row + 1, column=column, sticky='w', padx=5, pady=8)

    entry = tk.Entry(frame, width=28, relief=tk.GROOVE, bd=2, font=("Arial", 11))
    entry.grid(row=row + 1, column=column + 1, pady=8, padx=10)
    entries[var_name] = entry

# Patient admit section
admit_label = tk.Label(frame, text="Patient Admit:", bg="#5D6D7E", fg="white", font=("Comic Sans MS", 12))
admit_label.grid(row=8, column=0, sticky='w', pady=10)

admit_var = tk.StringVar(value="No")
yes_button = tk.Radiobutton(frame, text="Yes", variable=admit_var, value="Yes", bg="#5D6D7E", font=("Comic Sans MS", 12))
no_button = tk.Radiobutton(frame, text="No", variable=admit_var, value="No", bg="#5D6D7E", font=("Comic Sans MS", 12))
yes_button.grid(row=8, column=1, sticky='w')
no_button.grid(row=8, column=1, sticky='e')

# Button inside the box - right aligned
calculate_button = tk.Button(
    frame, text="Calculate Total Fees", command=calculate_total,
    font=("Comic Sans MS", 13, "bold"), bg="black", fg="white", relief=tk.RAISED, bd=4,
    padx=10, pady=4
)
calculate_button.grid(row=8, column=3, pady=20, sticky='e')

# Total Fees display - full-width centered
total_fees_label = tk.Label(
    frame, text="Total Fees: ₹ 0.00", font=("Comic Sans MS", 16, "bold"),
    bg="#D5D8DC", fg="black", relief=tk.SUNKEN, bd=2, padx=20, pady=8
)
total_fees_label.grid(row=9, column=0, columnspan=4, pady=15)

# Start the GUI loop
root.mainloop()
