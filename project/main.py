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
search_window.geometry('1200x800+300+200')
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
update_game = UpdateGame(update_window, connection)
btn_back_update = Button(update_window, text='Back', cnf=config_btns, command=lambda:change_window(management_window, update_window))
update_game.grid()
btn_back_update.grid()
#################  end Update window window widgets ################


##################   Search window widgets ################
def search():
    games = connection.search(e_name.get(), e_company.get(), e_age.get(), e_min_price.get(),e_max_price.get(), e_console.get(), e_min_stock.get(), e_max_stock.get())
    treev.delete(*treev.get_children())
    for game in games:
        treev.insert("", 'end', text =game[0], values =(game[1:8]))

treev = ttk.Treeview(search_window, selectmode ='browse')
treev.grid(row=1, column=1, columnspan=10)
verscrlbar = ttk.Scrollbar(search_window, orient ="vertical", command = treev.yview)
verscrlbar.grid(row=1, column=11, sticky='ns')
btn_back_search = Button(search_window, cnf=config_btns, text="Back", command=lambda:change_window(root, search_window))
Label(search_window, cnf=config_labels, text='Search by Name: ').grid(row=2, column=1)
Label(search_window, cnf=config_labels, text='Search by Company: ').grid(row=3, column=1)
Label(search_window, cnf=config_labels, text='Search by Age: ').grid(row=4, column=1)
Label(search_window, cnf=config_labels, text='Search by Min Price: ').grid(row=5, column=1)
Label(search_window, cnf=config_labels, text='Search by Max Price: ').grid(row=6, column=1)
Label(search_window, cnf=config_labels, text='Search by Console: ').grid(row=7, column=1)
Label(search_window, cnf=config_labels, text='Search by Min Stock: ').grid(row=8, column=1)
Label(search_window, cnf=config_labels, text='Search by Max Stock: ').grid(row=9, column=1)
e_name = Entry(search_window, cnf=config_entry)
e_company = Entry(search_window, cnf=config_entry)
e_age = Entry(search_window, cnf=config_entry)
e_min_price = Entry(search_window, cnf=config_entry)
e_max_price = Entry(search_window, cnf=config_entry)
e_console = Entry(search_window, cnf=config_entry)
e_min_stock = Entry(search_window, cnf=config_entry)
e_max_stock = Entry(search_window, cnf=config_entry)
e_name.grid(row=2, column=2)
e_company.grid(row=3, column=2)
e_age.grid(row=4, column=2)
e_min_price.grid(row=5, column=2)
e_max_price.grid(row=6, column=2)
e_console.grid(row=7, column=2)
e_min_stock.grid(row=8, column=2)
e_max_stock.grid(row=9, column=2)
btn_back_search.grid(row=6, rowspan=2, column=3, sticky='news')
btn_search_search = Button(search_window, cnf=config_btns, text="Search", command=search)
btn_search_search.grid(row=3, rowspan=2, column=3, sticky='news')

treev.configure(yscrollcommand = verscrlbar.set)
treev["columns"] = ("1", "2", "3", "4", "5", "6")
treev['show'] = 'headings'
treev.column("1", width = 150, anchor ='c')
treev.column("2", width = 120, anchor ='c')
treev.column("3", width = 75, anchor ='c')
treev.column("4", width = 120, anchor ='c')
treev.column("5", width = 120, anchor ='c')
treev.column("6", width = 75, anchor ='c')
treev.heading("1", text ="Name")
treev.heading("2", text ="Company")
treev.heading("3", text ="Age")
treev.heading("4", text ="Price")
treev.heading("5", text ="Console")
treev.heading("6", text ="Stock")
#################  Search window widgets ################
btn_management = Button(root, text='Management', cnf=config_btns, command=lambda:change_window(management_window, root))
btn_search = Button(root, text='Search', cnf=config_btns, command=lambda:change_window(search_window, root))
btn_management.pack(cnf=config_btns_root_pack)
btn_search.pack(cnf=config_btns_root_pack)

games = connection.get_all()
for game in games:
    treev.insert("", 'end', text =game[0], values =(game[1:8]))

root.mainloop()