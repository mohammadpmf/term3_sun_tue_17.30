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
