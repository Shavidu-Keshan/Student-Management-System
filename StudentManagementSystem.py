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
        
        entry_index=Entry(self.root,font=('calibri', 20, ),bg='lightgreen', fg='black',justify=RIGHT)
        entry_index.place(x=220, y=120, height=30,width=200)
        
        entry_index.focus()
        
        
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()