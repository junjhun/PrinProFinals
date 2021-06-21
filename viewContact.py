from tkinter import *
from myFormat import *

class titleFrame(Frame):
    def __init__(self, container0):
        super().__init__(container0)

        titleLabel = Label(self, text="View Contact", font=Fonts.fontTitle, pady=50)
        titleLabel.pack()

class viewContact(Frame):
    def __init__(self, container):
        super().__init__(container)
        contactsFile = open("contact.txt", "r")
        contentsDict = contactsFile.read()
        print(contentsDict["fname"])

        fnameLabel = Label(self, text="First Name", font=Fonts.labelFormat)
        lnameLabel = Label(self, text="Last Name", font=Fonts.labelFormat)
        fnameText = Label(self, bg="white", width=30)
        lnameText = Label(self, bg="white", width=30)
        pnumberLabel = Label(self, text="Phone Number: ", font=Fonts.labelFormat)
        pnumberText = Label(self, bg="white", width=30)
        emailLabel = Label(self, text="Email Address: ", font=Fonts.labelFormat)
        emailText = Label(self, bg="white", width=30)
        deptLabel = Label(self, text="Department: ", font=Fonts.labelFormat)
        deptText = Label(self, bg="white", width=30)

        fnameLabel.grid(row=0, column=0)
        lnameLabel.grid(row=1, column=0)
        fnameText.grid(row=0, column=1, padx=5)
        lnameText.grid(row=1, column=1, padx=5)
        pnumberLabel.grid(row=2, column=0, padx=5)
        pnumberText.grid(row=2, column=1, padx=5)
        emailLabel.grid(row=3, column=0)
        emailText.grid(row=3, column=1)
        deptLabel.grid(row=4, column=0)
        deptText.grid(row=4, column=1)


root = Tk()
frame0 = titleFrame(root)
frame0.pack()
frame1 = viewContact(root)
frame1.pack()
root.geometry("480x480")
root.title("View Contacts")
root.mainloop()