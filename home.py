from tkinter import *
window =Tk()
window.geometry("480x480")
window.title("Home")
class Fonts():
    fontTitle = ("arial",18,"bold")
    fontButton = ("arial",16)

welcomeNote=Label(window,text="Welcome to your PhoneBook",font=Fonts.fontTitle).pack()

def button():
    window.destroy()
    import addContact

addContactButton=Button(window,text="Add a Contact",bg='white',font=Fonts.fontButton,command=button).pack()
viewContactsButton=Button(window,text="View Contacts",bg='white',font=Fonts.fontButton).pack()


window.mainloop()