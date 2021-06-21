from tkinter import *
from myFormat import *

class titleFrame(Frame):
    def __init__(self, container0):
        super().__init__(container0)

        titleLabel = Label(self, text="Add a Contact", font=Fonts.fontTitle, pady=50)
        titleLabel.pack()

class formFrame(Frame):
    def __init__(self, container1):
        super().__init__(container1)

        fname = StringVar()
        lname = StringVar()
        pnumber = StringVar()
        email = StringVar()
        dept = StringVar

        fnameLabel = Label(self, text="First Name", font=Fonts.labelFormat)
        lnameLabel = Label(self, text="Last Name", font=Fonts.labelFormat)
        fnameEntry = Entry(self, bg="white", width=30, textvariable=fname)
        lnameEntry = Entry(self, bg="white", width=30, textvariable=lname)
        pnumberLabel = Label(self, text="Phone Number: ", font=Fonts.labelFormat)
        pnumberEntry = Entry(self, bg="white", width=30, textvariable=pnumber)
        emailLabel = Label(self, text="Email Address: ", font=Fonts.labelFormat)
        emailEntry = Entry(self, bg="white", width=30, textvariable=email)
        deptLabel = Label(self, text="Department: ", font=Fonts.labelFormat)
        deptEntry = Entry(self, bg="white", width=30, textvariable=dept)

        fnameLabel.grid(row=0, column=0)
        lnameLabel.grid(row=1, column=0)
        fnameEntry.grid(row=0, column=1, padx=5)
        lnameEntry.grid(row=1, column=1, padx=5)
        pnumberLabel.grid(row=2, column=0, padx=5)
        pnumberEntry.grid(row=2, column=1, padx=5)
        emailLabel.grid(row=3, column=0)
        emailEntry.grid(row=3, column=1)
        deptLabel.grid(row=4, column=0)
        deptEntry.grid(row=4, column=1)

class buttonFrame(Frame):
    def __init__(self, container2):
        super().__init__(container2)

        add = Button(self, text="Add Contact", font=Fonts.fontButton, command=self.add)
        cancel = Button(self, text="Cancel", font=Fonts.fontButton, command=self.cancel)

        add.grid(row=0, column=0)
        cancel.grid(row=0, column=1)

    def add(self):
        contactsFile = open("contact.txt", "a+")
        formFrame.__init__(self, container1="")
        contactsFile.write(formFrame.__init__.fname)
        contactsFile.close()
        import home

    def cancel(self):
        root.destroy()
        import home

root = Tk()
frame0 = titleFrame(root)
frame0.pack()
frame1 = formFrame(root)
frame1.pack()
frame2 = buttonFrame(root)
frame2.pack(pady=30)
root.geometry("480x480")
root.title("Add a Contact")
root.mainloop()