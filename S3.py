from tkinter import *
class Form():
    def __init__(self, root, bg=None, fg=None, bg2=None, fg2=None, font=None):
        self.r = root
        self.root = LabelFrame(self.r, text="Information", bg=bg, fg=fg, font=font)
        self.label_name = Label(self.root, text="Name: ", bg=bg, fg=fg, font=font)
        self.label_surname = Label(self.root, text="Surname: ", bg=bg, fg=fg, font=font)
        self.label_age = Label(self.root, text="Age: ", bg=bg, fg=fg, font=font)
        self.entry_name = Entry(self.root, bg=bg2, fg=fg2, font=font)
        self.entry_surname = Entry(self.root, bg=bg2, fg=fg2, font=font)
        self.spin_age = Spinbox(self.root, from_=1, to=99, font=font)
        self.btn_save = Button(self.root, text='Save',bg=bg, fg=fg, font=font, command=self.save)
        self.btn_reset = Button(self.root, text='Reset',bg=bg, fg=fg, font=font, command=self.reset)
        self.label_name.grid(row=1, column=1)
        self.label_surname.grid(row=2, column=1)
        self.label_age.grid(row=3, column=1)
        self.entry_name.grid(row=1, column=2)
        self.entry_surname.grid(row=2, column=2)
        self.spin_age.grid(row=3, column=2)
        self.btn_save.grid(row=4, column=1)
        self.btn_reset.grid(row=4, column=2)
    def reset(self):
        self.entry_name.delete(0, END)
        self.entry_surname.delete(0, END)
        self.spin_age.delete(0, END)
        self.spin_age.insert(0, 1)
        self.entry_name.focus_set()
    def save(self):
        f = open(f"{self.entry_name.get()} {self.entry_surname.get()}", "w")
        f.write(f"{self.entry_name.get()}\n{self.entry_surname.get()}\n{self.spin_age.get()}")
        f.close()
    def grid(self, row=1, column=1):
        self.root.grid(row=row, column=column)
root=Tk()
f1 = Form(root, bg='#333333', fg='orange')
f1.grid(row=1, column=1)
f2 = Form(root, bg='skyblue', fg='green', fg2='red')
f2.grid(row=2, column=1)
f3 = Form(root, font=('', 16))
f3.grid(row=3, column=1)
f4=Form(root, fg2='purple', bg='cyan', font=('Tahoma', 16))
f4.grid(row=1, column=2)
root.mainloop()