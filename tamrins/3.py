from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import json
class PersonalForm():
    def __init__(self, root, title = 'Patient\'s Personal Information', l1='Name: ', l2='Surname: ', l3='Father Name:',
                 l4='National Code: ', l5='Age: ', l6='Blood Type', padx=10, pady=10, bg=None, fg=None, font=None):
        self.root = root
        self.frame = LabelFrame(self.root, text=title, bg=bg, fg=fg, font=font, labelanchor='n', padx=padx, pady=pady)
        self.label1 = Label(self.frame, text=l1, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.label2 = Label(self.frame, text=l2, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.label3 = Label(self.frame, text=l3, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.label4 = Label(self.frame, text=l4, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.label5 = Label(self.frame, text=l5, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.label6 = Label(self.frame, text=l6, bg=bg, fg=fg, font=font, padx=padx, pady=pady)
        self.entry1 = Entry(self.frame, bg=bg, fg=fg, font=font)
        self.entry2 = Entry(self.frame, bg=bg, fg=fg, font=font)
        self.entry3 = Entry(self.frame, bg=bg, fg=fg, font=font)
        self.entry4 = Entry(self.frame, bg=bg, fg=fg, font=font)
        self.age = Spinbox(self.frame, from_=1, to=99, state='readonly', readonlybackground=bg, width=20, wrap=True, justify='center', fg=fg, font=font)
        self.blood_type = Combobox(self.frame, values=['A', 'B', 'O', 'AB'], justify='center', state='readonly', width=20, font=font)
        self.btnreset = Button(self.frame, text='Reset', bg=bg, fg=fg, font=font, padx=padx, pady=pady, command=self.reset)
        self.btnsave = Button(self.frame, text='Save', bg=bg, fg=fg, font=font, padx=padx, pady=pady, command=self.save)
        self.label1.grid(row=1, column=1, sticky='news')
        self.label2.grid(row=2, column=1, sticky='news')
        self.label3.grid(row=3, column=1, sticky='news')
        self.label4.grid(row=4, column=1, sticky='news')
        self.label5.grid(row=5, column=1, sticky='news')
        self.label6.grid(row=6, column=1, sticky='news')
        self.entry1.grid(row=1, column=2, sticky='news')
        self.entry2.grid(row=2, column=2, sticky='news')
        self.entry3.grid(row=3, column=2, sticky='news')
        self.entry4.grid(row=4, column=2, sticky='news')
        self.age.grid(row=5, column=2, sticky='news')
        self.blood_type.grid(row=6, column=2, sticky='news')
        self.btnreset.grid(row=7, column=1, sticky='news')
        self.btnsave.grid(row=7, column=2, sticky='news')
        self.reset()
    def save(self):
        f_name = filedialog.asksaveasfilename()
        f_name+='.json'
        f = open(f_name, 'w')
        info = {
            'Name': self.entry1.get(),
            'Surname': self.entry2.get(),
            'Father Name': self.entry3.get(),
            'National Code': self.entry4.get(),
            'Age': self.age.get(),
            'Blood Type': self.blood_type.get(),
        }
        json.dump(info, f, indent=4, ensure_ascii=False)
        f.close()
    def reset(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.age.config(state='normal')
        self.age.delete(0, END)
        self.age.insert(0, 12)
        self.age.config(state='readonly')
        self.blood_type.config(state='normal')
        self.blood_type.delete(0, END)
        self.blood_type.insert(0, 'A')
        self.blood_type.config(state='readonly')
        self.entry1.focus_set()
        
    def grid(self, row=None, column=None):
        self.frame.grid(row=row, column=column)

root = Tk()
form1 = PersonalForm(root, bg='sky blue', fg='purple', font=('Serif', 20))
form1.grid()
mainloop()