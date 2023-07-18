from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1000x500+100+50")
        self.root.resizable(False, False)

        self.bg=ImageTk.PhotoImage(file="image/1.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=370, y=9, width=500, height=400)

        title=Label(Frame_login, text="Login", font=("Tahoma", 35, "bold"), fg="#6162FF", bg="white").place(x=185,y=30)
        subtitle=Label(Frame_login, text="SMART ATTENDANCE CHECKING SYSTEM", font=("Tahoma", 12), fg="#1d1d1d", bg="white").place(x=85,y=100)

        lbl_user=Label(Frame_login, text="Username", font=("Tahoma", 15, "bold"), fg="grey", bg="white").place(x=85,y=140)
        self.username=Entry(Frame_login, font=("Tahoma", 15), bg="#E7E6E6")
        self.username.place(x=85,y=170, width=320, height=35)

        lbl_password=Label(Frame_login, text="Password", font=("Tahoma", 15, "bold"), fg="grey", bg="white").place(x=85,y=210)
        self.password=Entry(Frame_login, font=("Tahoma", 15), bg="#E7E6E6")
        self.password.place(x=85,y=240, width=320, height=35)

        forget=Button(Frame_login, text="Forgot Password?",bd=0, cursor="hand2",font=("Tahoma", 15), fg="#6162FF", bg="white").place(x=85,y=280)
        submit=Button(Frame_login,command=self.check_function,cursor="hand2", text="Login",bd=0, font=("Tahoma", 15), bg="#6162FF", fg="white").place(x=85,y=320, width=180, height=40)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required to login", parent=self.root)
        elif self.username.get() != "admin" or self.password.get() != "123456":
                messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        else:
                messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root=Tk()
obj=Login(root)
root.mainloop()