from tkinter import *
class Form():
    def __init__(self, root, bg=None, fg=None, bg2=None, fg2=None):
        self.r = root
        self.root = LabelFrame(self.r, text="Information", bg=bg, fg=fg)
        self.label_name = Label(self.root, text="Name: ", bg=bg, fg=fg)
        self.label_surname = Label(self.root, text="Surname: ", bg=bg, fg=fg)
        self.label_age = Label(self.root, text="Age: ", bg=bg, fg=fg)
        self.entry_name = Entry(self.root, bg=bg2, fg=fg2)
        self.entry_surname = Entry(self.root, bg=bg2, fg=fg2)
        self.spin_age = Spinbox(self.root, from_=1, to=99)
        self.btn_save = Button(self.root, text='Save',bg=bg, fg=fg)
        self.label_name.grid(row=1, column=1)
        self.label_surname.grid(row=2, column=1)
        self.label_age.grid(row=3, column=1)
        self.entry_name.grid(row=1, column=2)
        self.entry_surname.grid(row=2, column=2)
        self.spin_age.grid(row=3, column=2)
        self.btn_save.grid(row=4, column=1)
    def grid(self):
        self.root.grid()
root=Tk()
f1 = Form(root, bg='#333333', fg='orange')
f1.grid()
f2 = Form(root, bg='skyblue', fg='green', fg2='red')
f2.grid()
f3 = Form(root)
f3.grid()
f4=Form(root, fg2='purple', bg='cyan', font=('Tahoma', 25))
f4.grid()
root.mainloop()
# اضافه کردن ویژگی فونت به کلاس فرم هست.
# اضافه کردن ویژگی های ردیف و ستون به تابع گرید از کلاس فرم