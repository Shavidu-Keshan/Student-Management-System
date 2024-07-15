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
        
        title = Label(self.root, text="Student Management System", font=('calibri', 30, 'bold'),
                      bg='lightgreen', fg='black', anchor='w', padx=20)
        title.place( y=30, relwidth=1, height=50)
        
        #title = Label(self.root, text="Student Name", font=('calibri', 30, 'bold'),
         #             bg='lightgreen', fg='black', anchor='w', padx=20)
        #title.place( y=30, relwidth=1, height=50)
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()