from tkinter import *
from myFormat import *
window =Tk()
window.geometry("480x480")
window.title("Add a Contact")

Label(window,text="Add a Contact",font=Fonts.fontTitle).pack()

Label(text="Name",font=Fonts.labelFormat).pack()
inputName = Text(window,height=1,width=30,bg="white").pack()
Label(text="Contact",font=Fonts.labelFormat).pack()
inputContact = Text(window,height=1,width=30,bg="white").pack()
Label(text="Email Address")

window.mainloop()