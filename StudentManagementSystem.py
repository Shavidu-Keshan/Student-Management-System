from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
from tkinter import ttk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x575+200+75")
        self.root.title("Student Management System")
        self.root.resizable(False, False)

        # Open and resize the image
        image = Image.open("school.jpg")
        resized_image = image.resize((1000, 575))  # Resize to fit the window size

        # Convert the resized image to PhotoImage
        self.photo_image = ImageTk.PhotoImage(resized_image)

        # Display the image in a label
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=0, y=0)

        title = Label(self.root, text="Student Management System", font=('times', 30, 'bold'),
                      bg='lightgreen', fg='black', anchor='w', padx=20)
        title.place(y=30, relwidth=1, height=50)

        lbl_index = Label(self.root, text="Index No", font=('times', 20, 'bold'),
                          bg='lightgreen', fg='black', anchor='w')
        lbl_index.place(x=10, y=120, height=30, width=200)

        lbl_name = Label(self.root, text="Student Name", font=('times', 20, 'bold'),
                         bg='lightgreen', fg='black', anchor='w')
        lbl_name.place(x=10, y=160, height=30, width=200)

        lbl_address = Label(self.root, text="Adress", font=('times', 20, 'bold'),
                            bg='lightgreen', fg='black', anchor='w')
        lbl_address.place(x=10, y=200, height=30, width=200)

        lbl_contact = Label(self.root, text="Contact", font=('times', 20, 'bold'),
                            bg='lightgreen', fg='black', anchor='w')
        lbl_contact.place(x=10, y=240, height=30, width=200)

        lbl_email = Label(self.root, text="Email", font=('times', 20, 'bold'),
                          bg='lightgreen', fg='black', anchor='w')
        lbl_email.place(x=10, y=280, height=30, width=200)

        lbl_class = Label(self.root, text="Class", font=('times', 20, 'bold'),
                          bg='lightgreen', fg='black', anchor='w')
        lbl_class.place(x=10, y=320, height=30, width=200)

        # Variables
        self.var_index = StringVar()
        self.var_name = StringVar()
        self.var_address = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_class = StringVar()

        # Text Entry
        entry_index = Entry(self.root, textvariable=self.var_index, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_index.place(x=220, y=120, height=30, width=200)
        entry_index.focus()

        entry_name = Entry(self.root, textvariable=self.var_name, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_name.place(x=220, y=160, height=30, width=400)

        entry_address = Entry(self.root, textvariable=self.var_address, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_address.place(x=220, y=200, height=30, width=400)

        entry_contact = Entry(self.root, textvariable=self.var_contact, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_contact.place(x=220, y=240, height=30, width=150)

        entry_email = Entry(self.root, textvariable=self.var_email, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_email.place(x=220, y=280, height=30, width=400)

        entry_class = Entry(self.root, textvariable=self.var_class, font=('times', 20), bg='lightgreen', fg='black', justify=RIGHT)
        entry_class.place(x=220, y=320, height=30, width=130)

        # Buttons
        btn_save = Button(self.root, text="Save", command=self.save, font=('times', 20, 'bold'), bg='lightblue', fg='black', activebackground="#6eb3e6", cursor='hand2')
        btn_save.place(x=10, y=375, height=30, width=100)

        btn_update = Button(self.root, text="Update", command=self.update, font=('times', 20, 'bold'), bg='lightblue', fg='black', activebackground="#6eb3e6", cursor='hand2')
        btn_update.place(x=130, y=375, height=30, width=100)

        btn_delete = Button(self.root, text="Delete", command=self.delete, font=('times', 20, 'bold'), bg='lightblue', fg='black', activebackground="#6eb3e6", cursor='hand2')
        btn_delete.place(x=250, y=375, height=30, width=100)

        btn_clear = Button(self.root, text="Clear", command=self.clear, font=('times', 20, 'bold'), bg='lightblue', fg='black', activebackground="#6eb3e6", cursor='hand2')
        btn_clear.place(x=370, y=375, height=30, width=100)

        # Treeview
        treeview_frame = Frame(self.root, bd=2, relief=RIDGE)
        treeview_frame.place(x=10, y=420, width=984, height=135)

        scrolly = Scrollbar(treeview_frame, orient=VERTICAL)
        scrollx = Scrollbar(treeview_frame, orient=HORIZONTAL)

        self.treeviewtable = ttk.Treeview(treeview_frame, columns=("indexno", "name", "adress", "contact", "email", "class"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.config(command=self.treeviewtable.xview)
        scrolly.config(command=self.treeviewtable.yview)

        self.treeviewtable.heading("indexno", text="Index No")
        self.treeviewtable.heading("name", text="Student Name")
        self.treeviewtable.heading("adress", text="Adress")
        self.treeviewtable.heading("contact", text="Contact")
        self.treeviewtable.heading("email", text="Email")
        self.treeviewtable.heading("class", text="Class")

        self.treeviewtable["show"] = "headings"
        self.treeviewtable.column("indexno", width=70)
        self.treeviewtable.column("name", width=150)
        self.treeviewtable.column("adress", width=150)
        self.treeviewtable.column("contact", width=80)
        self.treeviewtable.column("email", width=100)
        self.treeviewtable.column("class", width=70)

        self.treeviewtable.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.treeviewtable.yview)

        self.displaydata()

    def displaydata(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="KE1120shan#", database="student")
        cur = sqlcon.cursor()
        cur.execute("SELECT indexno, name, adress, contact, email, class FROM student")
        result = cur.fetchall()

        self.treeviewtable.delete(*self.treeviewtable.get_children())
        for row in result:
            self.treeviewtable.insert("", END, values=row)
        sqlcon.close()

    def clear(self):
        self.var_index.set("")
        self.var_name.set("")
        self.var_address.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_class.set("")

    def save(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="KE1120shan#", database="student")
        cur = sqlcon.cursor()
        try:
            if self.var_index.get() == "":
                messagebox.showerror("Error", "All fields are required!")
            else:
                cur.execute("INSERT INTO student (indexno, name, adress, contact, email, class) VALUES(%s, %s, %s, %s, %s, %s)",
                            (
                                self.var_index.get(),
                                self.var_name.get(),
                                self.var_address.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_class.get(),
                            ))
                sqlcon.commit()
                messagebox.showinfo("Success", "Record inserted successfully")
                self.displaydata()
                self.clear()
                sqlcon.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def update(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="KE1120shan#", database="student")
        cur = sqlcon.cursor()
        try:
            if self.var_index.get() == "":
                messagebox.showerror("Error", "All fields are required!")
            else:
                cur.execute("UPDATE student SET name=%s, adress=%s, contact=%s, email=%s, class=%s WHERE indexno=%s",
                            (
                                self.var_name.get(),
                                self.var_address.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_class.get(),
                                self.var_index.get()
                            ))
                sqlcon.commit()
                messagebox.showinfo("Success", "Record updated successfully")
                self.displaydata()
                self.clear()
                sqlcon.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        sqlcon = pymysql.connect(host="localhost", user="root", password="KE1120shan#", database="student")
        cur = sqlcon.cursor()
        try:
            if self.var_index.get() == "":
                messagebox.showerror("Error", "Index No is required!")
            else:
                cur.execute("DELETE FROM student WHERE indexno=%s", self.var_index.get())
                sqlcon.commit()
                messagebox.showinfo("Success", "Record deleted successfully")
                self.displaydata()
                self.clear()
                sqlcon.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
