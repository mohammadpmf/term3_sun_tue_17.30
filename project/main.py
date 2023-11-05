from tkinter import *
from settings import *
from my_class import *

def change_window(show_window, hide_window):
    pass

connection = MyConnection()
root = Tk()
root.geometry('400x200+300+200')
root.config(bg=BG)
management_window = Toplevel(root)
search_window = Toplevel(root)
add_window = Toplevel(management_window)
update_window = Toplevel(management_window)
delete_window = Toplevel(management_window)
management_window.withdraw()
search_window.withdraw()
add_window.withdraw()
update_window.withdraw()
delete_window.withdraw()
management_window.config(bg=BG)
search_window.config(bg=BG)
add_window.config(bg=BG)
update_window.config(bg=BG)
delete_window.config(bg=BG)

##################   management window widgets ################
btn_add = Button(management_window, text='Add A Game', cnf=config_btns)
btn_update = Button(management_window, text='Update A Game', cnf=config_btns)
btn_delete = Button(management_window, text='Delete A Game', cnf=config_btns)
btn_add.pack(cnf=config_btns_root_pack)
btn_update.pack(cnf=config_btns_root_pack)
btn_delete.pack(cnf=config_btns_root_pack)
#################  end management window widgets ################

btn_management = Button(root, text='Management', cnf=config_btns, command=lambda:change_window(management_window, root))
btn_search = Button(root, text='Search', cnf=config_btns)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
root.mainloop()