from tkinter import *
from tkinter import messagebox

root=Tk()
top = Tk()
root.title("login format")
root.geometry("250x300")
top.geometry("500x600")

uname = Label(root, text='username').grid(row=1, column=0)
pswd = Label(root, text='password').grid(row=2, column=0)

e1=Entry(root)
e1.place(x=70, y=5)
e2=Entry(root)
e2.place(x=70, y=35)
def login():
    uname= e1.get()
    pswd = e2.get()

    if (uname==" " and pswd==" ") :
        messagebox.showinfo(" ", "blank now allowed")

    elif(uname =='admin' and pswd =='deepak'):
        messagebox.showinfo("", "Login Successful")
        root.destroy()
        c = Canvas(top, bg="Red", height="200")
        c.create_arc(5, 20, 140, 200, start=0, extent=150, fill="Green")
        c.pack()
        top.mainloop()

    else:
        messagebox.showinfo("", "username or password is incorrect")


Button(root,text="login", command=login, height=1, width=4).place(x=150, y=65)

root.mainloop()