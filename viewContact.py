import csv
from tkinter import *
from myFormat import *
import glob

class titleFrame(Frame):
    def __init__(self, container0):
        super().__init__(container0)

        titleLabel = Label(self, text="View Contact", font=Fonts.fontTitle, pady=10)
        titleLabel.pack()

class viewContact(Frame):
    def __init__(self, container):
        super().__init__(container)

        self.contactListBox = Listbox(self)
        for file_name in glob.iglob("source/*.csv", recursive=True):
            self.contactListBox.insert(END, file_name)
        self.contactListBox.grid(row=0, column=0, columnspan = 2, pady=10)

        self.fname = StringVar()
        self.lname = StringVar()
        self.pnumber = StringVar()
        self.email = StringVar()
        self.dept = StringVar()

        fnameLabel = Label(self, text="First Name", font=Fonts.labelFormat)
        lnameLabel = Label(self, text="Last Name", font=Fonts.labelFormat)
        fnameText = Label(self, bg="white", width=30, text=self.fname)
        lnameText = Label(self, bg="white", width=30, text=self.lname)
        pnumberLabel = Label(self, text="Phone Number: ", font=Fonts.labelFormat)
        pnumberText = Label(self, bg="white", width=30, text=self.pnumber)
        emailLabel = Label(self, text="Email Address: ", font=Fonts.labelFormat)
        emailText = Label(self, bg="white", width=30, text=self.email)
        deptLabel = Label(self, text="Department: ", font=Fonts.labelFormat)
        deptText = Label(self, bg="white", width=30, text=self.dept)

        fnameLabel.grid(row=1, column=0)
        lnameLabel.grid(row=2, column=0)
        fnameText.grid(row=1, column=1, padx=5)
        lnameText.grid(row=2, column=1, padx=5)
        pnumberLabel.grid(row=3, column=0, padx=5)
        pnumberText.grid(row=3, column=1, padx=5)
        emailLabel.grid(row=4, column=0)
        emailText.grid(row=4, column=1)
        deptLabel.grid(row=5, column=0)
        deptText.grid(row=5, column=1)

        editButton = Button(self, text="View Contact", font=Fonts.fontButton, bg="white",
                            command=self.view_item)
        editButton.grid(row=6, column=0)
        deleteButton = Button(self,text="Delete Contact", font=Fonts.fontButton, bg="white")
        deleteButton.grid(row=6, column=1)

    def view_item(self):
        selectedContact = self.contactListBox.curselection()
        index = selectedContact[0]
        value = self.contactListBox.get(index)
        print (value)
        # contactDict = {}
        file = open(value, 'r')
        reader = csv.DictReader(file)
        # print (file)
        orderedDict = list(reader)[0]
        contactDict = dict(orderedDict)
        # contactDict = {rows[0]:rows[1] for rows in reader}
        print (contactDict)

        self.fname.set = contactDict['fname']
        self.lname.set = contactDict['lname']
        self.pnumber.set = contactDict['pnumber']
        self.email.set = contactDict['email']
        self.dept.set = contactDict['dept']

root = Tk()
frame0 = titleFrame(root)
frame0.pack()
frame1 = viewContact(root)
frame1.pack()
root.geometry("480x480")
root.title("View Contacts")
root.mainloop()