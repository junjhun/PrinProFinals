from tkinter import *
from myFormat import *
window = Tk()
window.geometry("480x480")
window.title("Home")

Label(window,text="Welcome to your PhoneBook",font=Fonts.fontTitle,pady=(100)).pack()

def addContact():
    window.destroy()
    import addContact

# Button for Add a Contact
Button(window,text="Add a Contact",bg='white',font=Fonts.fontButton,command=addContact).pack()

# Button for View Contacts
Button(window,text="View Contacts",bg='white',font=Fonts.fontButton).pack()


window.mainloop()