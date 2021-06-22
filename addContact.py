import csv
import tkinter.messagebox
import os.path
from os import path
from tkinter import *
from myFormat import *
root = Tk()
class titleFrame(Frame):
    def __init__(self, container0):
        super().__init__(container0)

        titleLabel = Label(self, text="Add a Contact", font=Fonts.fontTitle, pady=50)
        titleLabel.pack()

# root.fname = StringVar()
# root.lname = StringVar()
# root.pnumber = StringVar()
# root.email = StringVar()
# root.dept = StringVar()

class formFrame(Frame):
    def __init__(self, container1):
        super().__init__(container1)

        self.fname = StringVar()
        self.lname = StringVar()
        self.pnumber = StringVar()
        self.email = StringVar()
        self.dept = StringVar()

        fnameLabel = Label(self, text="First Name", font=Fonts.labelFormat)
        lnameLabel = Label(self, text="Last Name", font=Fonts.labelFormat)
        fnameEntry = Entry(self, bg="white", width=30, textvariable=self.fname)
        lnameEntry = Entry(self, bg="white", width=30, textvariable=self.lname)
        pnumberLabel = Label(self, text="Phone Number: ", font=Fonts.labelFormat)
        pnumberEntry = Entry(self, bg="white", width=30, textvariable=self.pnumber)
        emailLabel = Label(self, text="Email Address: ", font=Fonts.labelFormat)
        emailEntry = Entry(self, bg="white", width=30, textvariable=self.email)
        deptLabel = Label(self, text="Department: ", font=Fonts.labelFormat)
        deptEntry = Entry(self, bg="white", width=30, textvariable=self.dept)

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

        # root.fname = fname
        # root.lname = lname
        # root.pnumber = pnumber
        # root.email = email
        # root.dept = dept

# class buttonFrame(Frame):
#     def __init__(self, container2):
#         super().__init__(container2)

        add = Button(self, text="Add Contact", font=Fonts.fontButton, command=self.add)
        cancel = Button(self, text="Cancel", font=Fonts.fontButton, command=self.cancel)

        add.grid(row=5, column=0)
        cancel.grid(row=5, column=1)

    def add(self):
        # if f"{self.fname.get()}_{self.lname.get()}.csv" not in "source/":
        file = f"{self.fname.get()}_{self.lname.get()}.csv"

        path = f"source/{file}"
        if os.path.isfile(path):
            tkinter.messagebox.showinfo(title="Notice!!!",
                                        message="Contact is already existing! Do View Contact to edit your contact there.")
        else:
            contactDict = {"fname": self.fname.get(),
            "lname": self.lname.get(), "pnumber": self.pnumber.get()
                           , "email": self.email.get(), "dept": self.dept.get()}
            # w = csv.writer(open(f"source/{self.fname.get()}_{self.lname.get()}.csv", "a+"))
            print (contactDict)
            print (contactDict.get('fname'))
            with open(f'source/{self.fname.get()}_{self.lname.get()}.csv', 'a+') as f:
                # writer = csv.writer(f)
                # keys = ['fname','lname','pnumber','email','dept']
                writer = csv.DictWriter(f, fieldnames=contactDict.keys())
                writer.writeheader()
                writer.writerow(contactDict)
                # for k, v in contactDict.items():
                #     writer.writerows(k, v)
            # for key, val in contactDict.items():
            #     w.writerow([key, val])
            # contactsFile = open("contact.txt", "a+")
            # contactsFile.write("fname: "+self.fname.get()+", lname: "
            #                +self.lname.get()+", pnumber: "+self.pnumber.get()+", email: "
            #                +self.email.get()+", dept: "+self.dept.get())
            # contactsFile.close()
            root.destroy()
            import home

    def cancel(self):
        root.destroy()
        import home

frame0 = titleFrame(root)
frame0.pack()
frame1 = formFrame(root)
frame1.pack()
# frame2 = buttonFrame(root)
# frame2.pack(pady=30)
root.geometry("480x480")
root.title("Add a Contact")
root.mainloop()