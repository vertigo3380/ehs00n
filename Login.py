from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import*
from tkinter import font
root = Tk()
root.config(bg="#0f5a5e")
root.geometry("360x200")


def getvals():
    print("Successfully registered")


Label(root, text="Registration Form", font="arial 18 bold").grid(row=0, column=3)

Fullname = Label(root, text="Fullname")
Phone = Label(root, text="Phone Number")
Gender = Label(root, text="Gender")
Academic = Label(root, text="Academic")
City = Label(root, text="city of Born")

Fullname.grid(row=1, column=2)
Phone.grid(row=2, column=2)
Gender.grid(row=3, column=2)
Academic.grid(row=4, column=2)
City.grid(row=5, column=2)


Fullnamevalue = StringVar
phonevalue = StringVar
Gendervalue = StringVar
Academicvalue = StringVar
Cityvalue = StringVar
checkvalue = IntVar

Fullnameentry = Entry(root, textvariable=Fullnamevalue)
Phoneentry = Entry(root, textvariable=phonevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Academicentry = Entry(root, textvariable=Academicvalue)
Cityentry = Entry(root, textvariable=Cityvalue)

Fullnameentry.grid(row=1, column=3)
Phoneentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
Academicentry.grid(row=4, column=3)
Cityentry.grid(row=5, column=3)

checkbtn = Checkbutton(
    text="Agree with terms and condition", variable=checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Confirm", command=getvals).grid(row=8, column=3)


root.mainloop()
