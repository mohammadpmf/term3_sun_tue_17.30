from tkinter import *
from settings import *
from my_class import *

connection = MyConnection()
root = Tk()
root.geometry('400x200+300+200')
root.config(bg="#333333")
btn_management = Button(root, text='Management', cnf=config_btns, width=12)
btn_search = Button(root, text='Search', cnf=config_btns, width=12)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
root.mainloop()