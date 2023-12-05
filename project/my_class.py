from fallah import *
from settings import *
from tkinter import messagebox
import pymysql

class MyConnection():
    def __init__(self, user='root', password='root'):
        self.db =pymysql.connect(host='127.0.0.1', user=user, password=password)
        self.cursor = self.db.cursor()
        query = "CREATE SCHEMA IF NOT EXISTS `term4`;"
        self.cursor.execute(query)
        query = "CREATE TABLE IF NOT EXISTS `term4`.`games` (`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NOT NULL,`company` VARCHAR(40) NULL,`age` TINYINT UNSIGNED NULL,`price` INT UNSIGNED NOT NULL,`console` VARCHAR(30) NULL,`stock` SMALLINT UNSIGNED NOT NULL,`image` VARCHAR(200) NULL,PRIMARY KEY (`id`),UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE);"
        self.cursor.execute(query)
    def insert(self, name, price, stock, company=None, age=0, console=None, address=None):
        query = "INSERT INTO `term4`.`games` (`name`, `company`, `age`, `price`, `console`, `stock`, `image`) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        values = name, company, age, price, console, stock, address
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            return 0
        except pymysql.err.IntegrityError:
            return 2
    def delete(self, name):
        query = "DELETE FROM `term4`.`games` WHERE `name`=%s"
        values = name
        result = self.cursor.execute(query, values)
        self.db.commit()
        return result
    
    def update(self, name, price, stock, old_name, company=None, age=0, console=None, address=None):
        query = "UPDATE `term4`.`games` SET name=%s, price=%s, stock=%s, company=%s, age=%s,\
              console=%s, image=%s WHERE `name`=%s;"
        values = name, price, stock, company, age, console, address, old_name
        result = self.cursor.execute(query, values)
        self.db.commit()
        print(result)
        return result

    def get_all(self):
        query = "SELECT * FROM `term4`.`games`;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get(self, name):
        query = "SELECT * FROM `term4`.`games` WHERE `name`=%s;"
        self.cursor.execute(query, name)
        return self.cursor.fetchone()
    

class AddGame(MyGame):
    def __init__(self, root, connection, bg='#333333', fg='orange', fg2='orange', text="Game Info", font=('Times', 20), bd=1, labelanchor='n', relief='raised', abg="orange", afg="#333333", padx=5, pady=5):
        super().__init__(root, bg, fg, fg2, text, font, bd, labelanchor, relief, abg, afg, padx, pady)
        self.connection = connection
        self.btn_save  = Button(self.frame, text='Save', cnf=config_btns, command=self.save)
        self.btn_reset = Button(self.frame, text='Reset', cnf=config_btns, command=self.reset)
        self.btn_save .grid(row=15, column=1, sticky='news', padx=padx, pady=pady)
        self.btn_reset.grid(row=15, column=3, sticky='news', padx=padx, pady=pady)
    
    def reset(self):
        super().reset()
        self.e_name.focus_set()

    def save(self):
        name = self.e_name.get()
        company = self.e_company.get()
        age = self.e_age.get()
        price = self.e_price.get()
        console = self.e_console_type.get()
        stock = self.e_stock.get()
        address = self.file_address
        if name=='':
            messagebox.showerror("Error", "You must fill Name of the game.")
            self.e_name.focus_set()
            return
        try:
            price = int(self.e_price.get())
        except:
            messagebox.showerror("Error", "You must fill price with a number.")
            self.e_price.delete(0, END)
            self.e_price.focus_set()
            return
        try:
            stock = int(self.e_stock.get())
        except:
            messagebox.showerror("Error", "You must fill stock with a number.")
            self.e_stock.delete(0, END)
            self.e_stock.focus_set()
            return
        if age=="":
            age=None
        if company=="":
            company=None
        if console=="":
            console=None
        result = self.connection.insert(name, price, stock, company, age, console, address)
        if result == 0:
            messagebox.showinfo("Success", f"Game {name} added successfully!")
        elif result==2:
            messagebox.showwarning("Duplicate", f"Game {name} already exsists in Table")

class UpdateGame(AddGame):
    def __init__(self, root, connection, bg='#333333', fg='orange', fg2='orange', text="Game Info", font=('Times', 20), bd=1, labelanchor='n', relief='raised', abg="orange", afg="#333333", padx=5, pady=5):
        super().__init__(root, connection, bg, fg, fg2, text, font, bd, labelanchor, relief, abg, afg, padx, pady)
        self.e_old = Entry(self.frame, bg=bg, fg=fg2, font=font, bd=bd, insertbackground=fg2)
        self.btn_search  = Button(self.frame, text='Search', cnf=config_btns, command=self.search)
        self.e_old.grid(row=0, column=3)
        self.btn_search.grid(row=0, column=1)
    def search(self):
        result = self.connection.get(self.e_old.get())
        if result not in [None, ()]:
            self.e_name.delete(0, END)
            self.e_company.delete(0, END)
            self.e_age.config(state='normal')
            self.e_age.delete(0, END)
            self.e_age.config(state='readonly')
            self.e_price.delete(0, END)
            self.e_console_type.delete(0, END)
            self.e_stock.delete(0, END)
            self.e_name.insert(0, result[1])
            if result[2]!=None:
                self.e_company.insert(0, result[2])
            if result[3] not in [0, None]:
                self.e_age.config(state='normal')
                self.e_age.insert(0, result[3])
                self.e_age.config(state='readonly')
            self.e_price.insert(0, result[4])
            if result[5]!=None:
                self.e_console_type.insert(0, result[5])
            self.e_stock.insert(0, result[6])
            self.file_address = result[7]

        
    def save(self):
        name = self.e_name.get()
        company = self.e_company.get()
        age = self.e_age.get()
        price = self.e_price.get()
        console = self.e_console_type.get()
        stock = self.e_stock.get()
        address = self.file_address
        old_name = self.e_old.get()
        if name=='':
            messagebox.showerror("Error", "You must fill Name of the game.")
            self.e_name.focus_set()
            return
        try:
            price = int(self.e_price.get())
        except:
            messagebox.showerror("Error", "You must fill price with a number.")
            self.e_price.delete(0, END)
            self.e_price.focus_set()
            return
        try:
            stock = int(self.e_stock.get())
        except:
            messagebox.showerror("Error", "You must fill stock with a number.")
            self.e_stock.delete(0, END)
            self.e_stock.focus_set()
            return
        if age=="":
            age=None
        if company=="":
            company=None
        if console=="":
            console=None
        result = self.connection.update(name, price, stock, old_name, company, age, console, address)
        if result == 1:
            messagebox.showinfo("Success", f"Game {name} updated successfully!")
        elif result==0:
            messagebox.showwarning("Warning", f"Game {name} is not in Table!")