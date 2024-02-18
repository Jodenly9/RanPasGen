from tkinter import *
import random
import string
from tkinter import messagebox


Window= Tk()
Window.title("Password Generator")
Window.config(bg="#FFC0CB")

Password = StringVar()
front_P = StringVar()
P_Long = IntVar()

def validate_Long(P_Long):
    if P_Long.get() > 33:
        messagebox.showerror("Error", "Maximum password length is 33 characters.")
        P_Long.set(33)

# function to generate the password
def rand_Pass():
    global front_P
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""
    #loop to generate the user given length for password
    for x in range(P_Long.get()):
        password = password + random.choice(pass1)
    if front_P.get() != "":
        password = front_P.get() + password
    Password.set(password)

#tkinter command to generate the gui
Window.iconbitmap("dice.ico")
Window.geometry("330x290")
Label(Window, text="Password Generator", font="calibri 18 bold", bg="#FFC0CB").pack()
Label(Window, text="Enter the first part of the Password ", bg="#FFC0CB").pack(pady=9)
Entry(Window, textvar= front_P).pack(pady=2)
Label(Window, text="Enter length of Password (Maximum of 33 Characters)", bg="#FFC0CB").pack(pady=9)
Entry(Window, textvar= P_Long).pack(pady=2)
P_Long.trace_add("write", lambda *args: validate_Long())

Button(Window, text="Generate Password", command=rand_Pass, bg="#FF69B4").pack(pady=15)
Entry(Window, textvar= Password).pack(pady=2)

Window.mainloop()