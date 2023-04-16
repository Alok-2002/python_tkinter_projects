from tkinter import *
from tkinter import messagebox
import mysql.connector

background="#22228B"
framebg="#EEEE2C"
framefg="#FFFF30"

global trial_no
trial_no=0

def trial():
    global trial_no

    trial_no+=1
    print("Trail No is: ",trial_no)
    if trial_no==3:
        messagebox.showwarning("Warning","You've Tried More Than Limit.....")
        root.destroy() #program close
        
def loginuser():
    username=user.get()
    password=code.get()

    if (username=="" or username=="UserID") or (password=="" or password=="Password"):
        messagebox.showerror("Entry Error","Type Username Or Password ")

    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="2030",database="student_registration")
            mycursor=mydb.cursor()
            print("Connected To Database!!")
        except:
            messagebox.showerror("Connection","Databse Connection Not Established")
            return
        command="Use student_registration"
        mycursor.execute(command)

        command="Select * from Login where Username=%s And Password=%s"
        mycursor.execute(command,(username,password))
        myresult= mycursor.fetchone()
        print(myresult)

        if myresult==None:
            messagebox.showinfo("Invalid","Invalid USerID And Password..")
            trial()
        else:
            messagebox.showinfo("Login","SuccessFully Login.....")
            root.destroy()

root = Tk()
root.title("Login System")
root.geometry("1250x700")
root.configure(bg=background)
root.resizable(True,True)

#icon image
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)

backgroundimage=PhotoImage(file="images/LOGIN.png")
Label(frame,image=backgroundimage).pack()

#user entry
def user_enter(e):
    user.delete(0,'end')

def user_leave():
    name=user.get()
    if name=="":
        user.insert(0,'UserID')

user=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial Bold",24))
user.insert(0,"UserID")
user.bind("<FocusIn>",user_enter)
user.bind("<FocusOut>",user_leave)
user.place(x=500,y=315)

#password entry
def password_enter(e):
    code.delete(0,'end')

def password_leave():
    if code.get()=="":
        code.insert(0,'Password')
        
code=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=("Arial Bold",24))
code.insert(0,"Password")
code.bind("<FocusIn>",password_enter)
code.bind("<FocusOut>",password_leave)
code.place(x=500,y=410)

#hide and show button
button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground='white')
        code.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye,activebackground='white')
        code.config(show="")
        button_mode=True

openeye=PhotoImage(file="images/openeye.png")
closeeye= PhotoImage(file="images/close eye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=780,y=410)

#login button
loginButton=Button(root,text="LOGIN",fg="white",bg="#1f5675",width=10,height=1,font=("arial",16,"bold"),bd=0,command=loginuser)
loginButton.place(x=570,y=600)

label=Label(root,text="Don't Have An Account ?",fg="#fff",bg="#00264d",font=("Comic Sans MS",12))
label.place(x=450,y=500)
registerButton=Button(root,width=10,text="Add New User",border=0,bg="#00264d",cursor='hand2',fg="#57a1f8")
registerButton.place(x=650,y=505)

root.mainloop()
