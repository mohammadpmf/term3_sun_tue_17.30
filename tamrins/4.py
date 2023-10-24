from tkinter import *

class SignUp():
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(self.root, text="Sign Up")
        self.label_username = Label(self.frame, text='Username: ')
        self.label_password1 = Label(self.frame, text='Password: ')
        self.label_password2 = Label(self.frame, text='re-password: ')
        self.entry_username = Entry(self.frame)
        self.entry_password1 = Entry(self.frame, show='*')
        self.entry_password2 = Entry(self.frame, show='*')
        self.bv = BooleanVar(self.frame)
        self.cbt = Checkbutton(self.frame, variable=self.bv, command=self.check)
        self.btn = Button(self.frame, text='Sign Up')
        self.label_username.grid(row=1, column=1)
        self.label_password1.grid(row=2, column=1)
        self.label_password2.grid(row=3, column=1)
        self.entry_username.grid(row=1, column=2)
        self.entry_password1.grid(row=2, column=2)
        self.entry_password2.grid(row=3, column=2)
        self.cbt.grid(row=2, column=3)
        self.btn.grid(row=4, column=1, columnspan=2)
    
    def check(self):
        if self.bv.get():
            self.entry_password1.config(show='')
            self.label_password2.grid_forget()
            self.entry_password2.grid_forget()
        else:
            self.entry_password1.config(show='*')
            self.label_password2.grid(row=3, column=1)
            self.entry_password2.grid(row=3, column=2)
    
    def grid(self):
        self.frame.grid()

root = Tk()
s1 = SignUp(root)
s1.grid()
mainloop()