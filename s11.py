import pymysql
def login():
    u = input("Enter username:")
    query = "SELECT * FROM `login_register`.`users` where username=%s;"
    cursor.execute(query, u)
    data = cursor.fetchone()
    if data == None:
        print("This account does not exsit.")
    else:
        p = input("Enter password:")
        if data[3] == p:
            print("Welcome")
        else:
            print("Wrong password")
def sign_up():
    f = input("Enter your full name: ")
    u = input("Enter username: ")
    query = "SELECT * FROM `login_register`.`users` where username=%s;"
    cursor.execute(query, u)
    data = cursor.fetchone()
    if data == None:
        p = input("Enter password: ")
        query = "INSERT INTO `login_register`.`users` (`full_name`, `username`, `password`) VALUES (%s, %s, %s);"
        values = (f,u,p)
        cursor.execute(query, values)
        db.commit()
    else:
        print("Username already taken.")

db = pymysql.connect(host='127.0.0.1', user='root', password='root')
cursor = db.cursor()
query = "CREATE SCHEMA IF NOT EXISTS `login_register` ;"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS `login_register`.`users` (\
  `id` INT NOT NULL AUTO_INCREMENT,\
  `full_name` VARCHAR(45) NULL,\
  `username` VARCHAR(45) NOT NULL,\
  `password` VARCHAR(45) NOT NULL,\
  PRIMARY KEY (`id`),\
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);"
cursor.execute(query)
message = "Press 1 to create account.\nPress 2 to Login.\n q to exit program: "
answer = input(message)
while answer not in ["1", "2", "q"]:
    answer = input(message)
if answer == "1":
    sign_up()
elif answer == "2":
    login()
elif answer == "q":
    exit()