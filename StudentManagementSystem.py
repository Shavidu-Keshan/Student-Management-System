from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

class student:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1000x500+200+100")
        self.root.title("student management system")
        self.root.resizable(False,False)
        
      
         # Open and resize the image
        image = Image.open("school.jpg")
        resized_image = image.resize((1000, 500))  # Resize to fit the window size

        # Convert the resized image to PhotoImage
        self.photo_image = ImageTk.PhotoImage(resized_image)

        # Display the image in a label
        self.lbl_photo_image = Label(self.root, image=self.photo_image, bd=0)
        self.lbl_photo_image.place(x=0, y=0)
        
        title = Label(self.root, text="Student Management System", font=('times', 30, 'bold'),
                      bg='lightgreen', fg='black', anchor='w', padx=20)
        title.place( y=30, relwidth=1, height=50)
        
        lbl_index = Label(self.root, text="Index No", font=('times', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_index.place(x=10, y=120, height=30,width=200)
        
        lbl_name = Label(self.root, text="Student Name", font=('times', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_name.place(x=10, y=160, height=30,width=200)
        
        
        lbl_adress = Label(self.root, text="Adress", font=('times', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_adress.place(x=10, y=200, height=30,width=200)
        
        lbl_contact = Label(self.root, text="Contact", font=('times', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_contact.place(x=10, y=240, height=30,width=200)
        
        
        lbl_email = Label(self.root, text="Email", font=('times', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_email.place(x=10, y=280, height=30,width=200)
        
        lbl_class = Label(self.root, text="Class", font=('timesi', 20, 'bold'),
                      bg='lightgreen', fg='black',anchor='w')
        lbl_class.place(x=10, y=320, height=30,width=200)
        
        #bl_name = Label(self.root, text="Student Name", font=('calibri', 20, 'bold'),
              #        bg='lightgreen', fg='black',justify=LEFT)
        #lbl_name.place(x=10, y=160, height=30,width=300)
        
        # variables #
        
        self.var_index=StringVar()
        self.var_name=StringVar()
        self.var_adrees=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_class=StringVar()
        
        # Text Entry #
        
        entry_index=Entry(self.root,textvariable=self.var_index,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_index.place(x=220, y=120, height=30,width=200)
        entry_index.focus()
        
        entry_name=Entry(self.root,textvariable=self.var_index,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_name.place(x=220, y=160, height=30,width=400)
        
        entry_adress=Entry(self.root,textvariable=self.var_adrees,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_adress.place(x=220, y=200, height=30,width=400)
        
        entry_contact=Entry(self.root,textvariable=self.var_contact,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_contact.place(x=220, y=240, height=30,width=150)
        
        entry_email=Entry(self.root,textvariable=self.var_email,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_email.place(x=220, y=280, height=30,width=400)
        
        entry_class=Entry(self.root,textvariable=self.var_class,font=('times', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_class.place(x=220, y=320, height=30,width=130)
        
        #buttons #
        btn_save=Button(self.root,text="Save" ,command=self.save(),font=('times', 20,'bold'),bg='lightblue', fg='black',activebackground="#6eb3e6",cursor='hand2').place(x=10, y=375, height=30,width=100)
        btn_update=Button(self.root,text="Update" ,font=('times', 20,'bold'),bg='lightblue', fg='black',activebackground="#6eb3e6",cursor='hand2').place(x=130, y=375, height=30,width=100)
        btn_delete=Button(self.root,text="Delete" ,font=('times', 20,'bold'),bg='lightblue', fg='black',activebackground="#6eb3e6",cursor='hand2').place(x=250, y=375, height=30,width=100)
        btn_create=Button(self.root,text="Clear" ,font=('times', 20,'bold'),bg='lightblue', fg='black',activebackground="#6eb3e6",cursor='hand2').place(x=370, y=375, height=30,width=100)
        
    def save(self):
        pass
        
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()