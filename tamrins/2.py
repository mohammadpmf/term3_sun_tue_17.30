from tkinter import *
class Login():
    def __init__(self, root, bg=None, fg=None, font=None):
        self.r = root
        self.root = LabelFrame(self.r, text="Login", bg=bg, fg=fg, font=font)
        self.label_username = Label(self.root, text="Username: ", bg=bg, fg=fg, font=font)
        self.label_password = Label(self.root, text="Password: ", bg=bg, fg=fg, font=font)
        self.entry_username = Entry(self.root, bg=bg, fg=fg, font=font)
        self.entry_password = Entry(self.root, bg=bg, fg=fg, font=font, show="•")
        self.show_password = BooleanVar(self.root)
        self.checkbutton = Checkbutton(self.root, bg=bg, fg=fg, variable=self.show_password, font=font, command=self.check)
        self.btn_login = Button(self.root, text='Enter',bg=bg, fg=fg, font=font)
        self.label_username.grid(row=1, column=1)
        self.label_password.grid(row=2, column=1)
        self.entry_username.grid(row=1, column=2)
        self.entry_password.grid(row=2, column=2)
        self.checkbutton.grid(row=2, column=3)
        self.btn_login.grid(row=3, column=1)
    def check(self):
        if self.show_password.get():
            self.entry_password.config(show="")
        else:
            self.entry_password.config(show="•")
    def grid(self, row=None, column=None):
        self.root.grid(row=row, column=column)
root=Tk()
f1 = Login(root, bg='#333333', fg='orange', font=('consolas', 24))
f1.grid()
root.mainloop()