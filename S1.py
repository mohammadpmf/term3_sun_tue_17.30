# from tkinter import *
# root = Tk()
# b1 = Button(root,fg='black')
# b2 = Label(root,fg='black')
# b3 = Radiobutton()
class Person():
    # initialize مقدار دهیه اولیه کردن
    def __init__(self,height=175,weight=75,name=None,surname=None,father_name=None):
        self.height=height
        self.weight=weight
        self.name=name
        self.surname=surname
        self.father_name=father_name
    def __str__(self):
        return f"My name is {self.name} {self.surname}. Height: {self.height}"
    def fullname(self):
        return f"My name is {self.name} {self.surname}."
p1 = Person(190, 66, 'amirali')
p2 = Person(170, 55, "Kian", "Kalantari", "Reza")
p3 = Person(172, 60, "Abolfazl", "Taghipour", "Mohammad")
p4 = Person(surname="Safa", height=178, father_name="Reza", weight=70, name="Hossein")
p5 = Person(name="Mehrpooya", surname="valizadeh")
print(p1)
print(p3.fullname())
# print(p1.name)
# print(p2.name)
# print(p3.name)
# print(p4.name)
# print(p5.name)