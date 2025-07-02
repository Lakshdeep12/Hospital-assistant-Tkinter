from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import subprocess

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("JIET'X ONE CLINIC")
        self.root.geometry("1540x800+0+0")
        self.root.configure(bg="#1C2833")

        lb1title = Label(self.root, bd=20, relief=RIDGE, text="JIET'X ONE CLINIC", fg="#2C3E50", bg="lightblue", font=("Comic Sans MS", 30, "bold"))
        lb1title.pack(side=TOP, fill=X)

        # Main DataFrame
        DataFrame = Frame(self.root, bd=16, relief=RIDGE, bg="#34495E")
        DataFrame.pack(pady=10, fill=X)

        # Patient Info Frame
        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 20, "bold"), text="Patient Information", bg="#34495E", fg="red")
        DataFrameLeft.pack(side=LEFT, fill=BOTH, expand=False, padx=10)

        self.left_entries = {}
        self.right_entries = {}

        patient_info_fields = [
            ("Patient Name", "D.O.B"),
            ("Patient ID", "Blood Group"),
            ("Aadhar No.", "Appointment Date"),
            ("Guardian Name", "Test Suggested"),
            ("Appointment With", "Phone No."),
            ("Last Checkup Date", ""),
            ("Sickness Type", ""),
            ("Age", ""),
            ("Gender", "")
        ]

        for row_idx, (left_label, right_label) in enumerate(patient_info_fields):
            Label(DataFrameLeft, text=left_label, font=("Arial", 10, "bold"), width=18, anchor='w', bg="light blue").grid(row=row_idx, column=0, padx=5, pady=5)

            if left_label == "Sickness Type":
                self.left_entries[left_label] = StringVar()
                menu = OptionMenu(DataFrameLeft, self.left_entries[left_label], "Allergy", "Immunity", "Deficiency", "Communicable")
                menu.grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
                menu.configure(bg="light blue", width=23)
            else:
                entry = Entry(DataFrameLeft, width=25, bg="light blue")
                entry.grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
                self.left_entries[left_label] = entry

            if right_label:
                Label(DataFrameLeft, text=right_label, font=("Arial", 10, "bold"), width=18, anchor='w', bg="light blue").grid(row=row_idx, column=2, padx=5, pady=5)

                if right_label == "Test Suggested":
                    self.right_entries[right_label] = StringVar()
                    menu = OptionMenu(DataFrameLeft, self.right_entries[right_label], "Yes", "No")
                    menu.grid(row=row_idx, column=3, padx=5, pady=5, sticky='we')
                    menu.configure(bg="light blue", width=23)
                else:
                    entry = Entry(DataFrameLeft, width=25, bg="light blue")
                    entry.grid(row=row_idx, column=3, padx=5, pady=5, sticky='we')
                    self.right_entries[right_label] = entry

        data_button_frame = Frame(DataFrameLeft, pady=10, bg="#2C3E50")
        data_button_frame.grid(row=10, column=0, columnspan=4)

        btn_add = Button(data_button_frame, text="ADD DATA", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.add_data)
        btn_add.pack(side=LEFT, padx=10)

        btn_clear = Button(data_button_frame, text="CLEAR", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.clear_fields)
        btn_clear.pack(side=LEFT, padx=10)

        btn_delete = Button(data_button_frame, text="DELETE", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.delete_data)
        btn_delete.pack(side=LEFT, padx=10)

        button_frame = Frame(DataFrameLeft, pady=10, bg="#2C3E50")
        button_frame.grid(row=11, column=0, columnspan=4)

        btn_logout = Button(button_frame, text="Log Out", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.root.quit)
        btn_logout.pack(side=LEFT, padx=10)

        btn_payment = Button(button_frame, text="Payment", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.open_payment)
        btn_payment.pack(side=LEFT, padx=10)

        btn_chatbot = Button(button_frame, text="Chatbot", width=15, font=("Arial", 10, "bold"), bg="light blue", fg="black", command=self.open_chatbot)
        btn_chatbot.pack(side=LEFT, padx=10)

        # Right Frame for prescription placeholder
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 18, "bold"), text="Prescription", bg="#34495E", fg="red")
        DataFrameRight.pack(side=RIGHT, fill=BOTH, expand=True, padx=10)

        # Detail Frame (Table at bottom)
        DetailFrame = Frame(self.root, bd=12, relief=RIDGE, bg="light blue")
        DetailFrame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 10))

        scroll_x = Scrollbar(DetailFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DetailFrame, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(DetailFrame,
                                           columns=("name", "dob", "pid", "blood", "aadhar", "appdate", "guardian", "test", "doctor", "phone", "lastcheck", "sickness", "age", "gender"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("name", text="Patient Name")
        self.hospital_table.heading("dob", text="D.O.B")
        self.hospital_table.heading("pid", text="Patient ID")
        self.hospital_table.heading("blood", text="Blood Group")
        self.hospital_table.heading("aadhar", text="Aadhar No.")
        self.hospital_table.heading("appdate", text="Appointment Date")
        self.hospital_table.heading("guardian", text="Guardian Name")
        self.hospital_table.heading("test", text="Test Suggested")
        self.hospital_table.heading("doctor", text="Appointment With")
        self.hospital_table.heading("phone", text="Phone No.")
        self.hospital_table.heading("lastcheck", text="Last Checkup")
        self.hospital_table.heading("sickness", text="Sickness Type")
        self.hospital_table.heading("age", text="Age")
        self.hospital_table.heading("gender", text="Gender")
        self.hospital_table["show"] = "headings"

        for col in self.hospital_table["columns"]:
            self.hospital_table.column(col, width=120)

        self.hospital_table.pack(fill=BOTH, expand=True)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lakshdeep",
            database="hospital_system"
        )
        self.cursor = self.db_connection.cursor()

    def add_data(self):
        try:
            values = {
                key: var.get() if isinstance(var, StringVar) else var.get()
                for key, var in {**self.left_entries, **self.right_entries}.items()
            }

            query = """
                INSERT INTO patient_info (
                    patient_id, patient_name, adhar_no, appointment_with, last_checkup_date,
                    sickness_type, age, gender, date_of_birth, blood_group,
                    appointment_date, test_suggested, phone_no, guardian_name
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                values["Patient ID"], values["Patient Name"], values["Aadhar No."],
                values["Appointment With"], values["Last Checkup Date"], values["Sickness Type"],
                values["Age"], values["Gender"], values["D.O.B"], values["Blood Group"],
                values["Appointment Date"], values["Test Suggested"], values["Phone No."], values["Guardian Name"]
            )

            self.cursor.execute(query, data)
            self.db_connection.commit()
            messagebox.showinfo("Success", "Patient record added successfully!")

            self.hospital_table.insert("", END, values=tuple(values[key] for key in [
                "Patient Name", "D.O.B", "Patient ID", "Blood Group", "Aadhar No.",
                "Appointment Date", "Guardian Name", "Test Suggested",
                "Appointment With", "Phone No.", "Last Checkup Date",
                "Sickness Type", "Age", "Gender"
            ]))
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        for entry in self.left_entries.values():
            if isinstance(entry, Entry):
                entry.delete(0, END)
            elif isinstance(entry, StringVar):
                entry.set("")
        for entry in self.right_entries.values():
            if isinstance(entry, StringVar):
                entry.set("")

    def delete_data(self):
        selected = self.hospital_table.focus()
        if not selected:
            messagebox.showwarning("Delete", "Please select a record to delete.")
            return

        values = self.hospital_table.item(selected, "values")
        patient_id = values[2] 

        try:
            self.cursor.execute("DELETE FROM patient_info WHERE patient_id = %s", (patient_id,))
            self.db_connection.commit()
            self.hospital_table.delete(selected)
            messagebox.showinfo("Deleted", "Record deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_chatbot(self):
        subprocess.Popen(["python", "app.py"])

    def open_payment(self):
        subprocess.Popen(["python", "patient_bill.py"])


root = Tk()
ob = Hospital(root)
root.mainloop()
