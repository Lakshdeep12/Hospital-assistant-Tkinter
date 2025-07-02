from tkinter import *
from tkinter import messagebox
import os
import sys

# Path to the folder containing the certificates
CERTIFICATE_FOLDER = r"C:\Users\HP\OneDrive\Desktop\chatbot\docs"

# List of certificates: tuple of filename, display name, and short description
CERTIFICATES = [
    ('death.docx', 'Death Certificate', 'Official document certifying death'),
    ('disability.docx', 'Disability Certificate', 'Proof of disability status'),
    ('Fitness.docx', 'Fitness Certificate', 'Health and fitness verification'),
    ('health certificate.docx', 'Health Certificate', 'Health status confirmation'),
    ('mental.docx', 'Mental Health Certificate', 'Mental health evaluation'),
    ('noc certificate.docx', 'No Objection Certificate', 'Permission clearance document'),
    ('vaccination certificate.docx', 'Vaccination Certificate', 'Vaccination proof document'),
    ('Medical certificate.docx', 'Medical Certificate', 'General medical certificate'),
]

def open_certificate(filename):
    certificate_path = os.path.join(CERTIFICATE_FOLDER, filename)
    if os.path.exists(certificate_path):
        try:
            if sys.platform.startswith('darwin'):
                # macOS
                os.system(f'open "{certificate_path}"')
            elif os.name == 'nt':
                # Windows
                os.startfile(certificate_path)
            elif os.name == 'posix':
                # Linux
                os.system(f'xdg-open "{certificate_path}"')
            else:
                messagebox.showerror("Unsupported OS", "Cannot open files on this operating system.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open certificate file:\n{str(e)}")
    else:
        messagebox.showerror("File Not Found", f"The certificate file was not found:\n{certificate_path}")

def create_gui():
    root = Tk()
    root.title("JIET'X ONE CLINIC")
    root.geometry("1240x700+0+0")
    root.configure(bg="#1C2833")

    # Title Label
    lb1title = Label(root, bd=20, relief=RIDGE, text="JIET'X ONE CLINIC",
                     fg="#1C2833", bg="lightblue", font=("Comic Sans MS", 30, "bold"))
    lb1title.pack(side=TOP, fill=X)

    # Main Frame
    MainFrame = Frame(root, bd=16, relief=RIDGE, bg="#34495E")
    MainFrame.place(x=10, y=100, width=1240, height=550)

    # Instruction Label
    label2 = Label(MainFrame,
                   text="Click a certificate button below to open your certificate file.",
                   wraplength=1150, justify="left",
                   bg="#1C2833", fg="white", font=("Comic Sans MS", 14, "bold"))
    label2.pack(pady=(10, 20), anchor='w', padx=20)

    # Buttons container Frame for left aligned buttons and descriptions
    buttons_frame = Frame(MainFrame, bg="#34495E")
    buttons_frame.pack(fill='both', expand=True, padx=20, anchor='w')

    for filename, display_name, description in CERTIFICATES:
        # Container frame for each button + description row
        row_frame = Frame(buttons_frame, bg="#34495E")
        row_frame.pack(fill='x', pady=5)

        # Button
        btn = Button(row_frame, text=display_name, width=25, height=2,
                     font=("Comic Sans MS", 9, "bold"), fg="#1C2833", bg="light blue",
                     activebackground="#0056b3",
                     command=lambda f=filename: open_certificate(f))
        btn.pack(side=LEFT)

        # Description label next to button
        desc_label = Label(row_frame, text=description,
                           bg="#34495E", fg="white",
                           font=("Comic Sans MS", 10))
        desc_label.pack(side=LEFT, padx=10, pady=10, anchor='w')

    root.mainloop()

if __name__ == "__main__":
    create_gui()
