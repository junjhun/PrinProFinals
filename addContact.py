from tkinter import *
from myFormat import *
window = Tk()
window.geometry("480x480")
window.title("Add a Contact")

mainFrame = Frame(window)
mainFrame.pack()
column1 = Frame(window)
column1.pack(side="left",expand=True)

Label(mainFrame,text="Add a Contact",font=Fonts.fontTitle,pady=(10)).pack()

Label(column1,text="Name",font=Fonts.labelFormat).pack()
inputName = Entry(column1,width=30,bg="white").pack()
Label(column1,text="Contact",font=Fonts.labelFormat).pack()
inputContact = Entry(column1,width=30,bg="white").pack()
Label(column1,text="Email Address",font=Fonts.labelFormat).pack()
inputEmail = Entry(column1,width=30,bg="white").pack()


window.mainloop()