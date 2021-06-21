from tkinter import *
from myFormat import *

class mainFrame(Frame):

    def __init__(self, container):
        super().__init__(container)

        title = Label(self, text="Welcome to your Phonebook", font=Fonts.fontTitle, pady=100)
        addContactButton = Button(self, text="Add a Contact", font=Fonts.fontButton, bg="white",
                                  command=self.addContactCommand)
        viewContactButton = Button(self, text="View your Contacts", font=Fonts.fontButton, bg="white")

        title.pack()
        addContactButton.pack()
        viewContactButton.pack()

    def addContactCommand(self):
        root.destroy()
        import addContact

    def viewContactCommand(self):
        root.destroy()
        # import viewContact

root = Tk()
frame1 = mainFrame(root)
frame1.pack()
root.geometry("480x480")
root.title("Home")
root.mainloop()