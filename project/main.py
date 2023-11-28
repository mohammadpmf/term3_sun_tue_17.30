from tkinter import *
from settings import *
from my_class import *

def change_window(show_window:Toplevel, hide_window:Toplevel):
    show_window.deiconify()
    hide_window.withdraw()

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
management_window.protocol("WM_DELETE_WINDOW", root.destroy)
search_window.protocol("WM_DELETE_WINDOW", root.destroy)
add_window.protocol("WM_DELETE_WINDOW", root.destroy)
update_window.protocol("WM_DELETE_WINDOW", root.destroy)
delete_window.protocol("WM_DELETE_WINDOW", root.destroy)
management_window.geometry('700x300+300+200')
search_window.geometry('500x300+300+200')
add_window.geometry('900x700+300+200')
update_window.geometry('900x700+300+200')
delete_window.geometry('600x180+300+200')
##################   management window widgets ################
btn_add = Button(management_window, text='Add A Game', cnf=config_btns,
                 command=lambda:change_window(add_window, management_window))
btn_update = Button(management_window, text='Update A Game', cnf=config_btns, command=lambda:change_window(update_window, management_window))
btn_delete = Button(management_window, text='Delete A Game', cnf=config_btns, command=lambda:change_window(delete_window, management_window))
btn_back_management = Button(management_window, text='Back', cnf=config_btns, command=lambda:change_window(root, management_window))
btn_add.pack(cnf=config_btns_root_pack)
btn_update.pack(cnf=config_btns_root_pack)
btn_delete.pack(cnf=config_btns_root_pack)
btn_back_management.pack(cnf=config_btns_root_pack)
#################  end management window widgets ################

##################   Add window widgets ################
game = AddGame(add_window, connection)
btn_back_add = Button(add_window, text='Back', cnf=config_btns, command=lambda:change_window(management_window, add_window))
game.grid()
btn_back_add.grid()
#################  end Add window window widgets ################

##################   Delete window widgets ################
def delete_game():
    game_name = entry_delete_game.get().strip()
    result = connection.delete(game_name)
    if result==1:
        messagebox.showinfo("Success", f"Game {game_name} deleted Successfully.")
    else:
        messagebox.showwarning("Warning", f"Game {game_name} does not exsist!")
Label(delete_window, text='Which Game you want to delete?', cnf=config_labels).grid(row=1, column=1)
entry_delete_game = Entry(delete_window, cnf=config_entry)
entry_delete_game.grid(row=1, column=2)
Button(delete_window, text='Delete this game', cnf=config_btns, command=delete_game).grid(row=2, column=1, columnspan=2, sticky='news')
Button(delete_window, text='Back', cnf=config_btns, command=lambda:change_window(management_window, delete_window)).grid(row=3, column=1, columnspan=2, sticky='news')
#################  end Delete window window widgets ################

##################   Update window widgets ################
update_game = AddGame(update_window, connection)
btn_back_update = Button(update_window, text='Back', cnf=config_btns, command=lambda:change_window(management_window, update_window))
update_game.grid()
btn_back_update.grid()
#################  end Update window window widgets ################

btn_management = Button(root, text='Management', cnf=config_btns, command=lambda:change_window(management_window, root))
btn_search = Button(root, text='Search', cnf=config_btns)
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)
root.mainloop()