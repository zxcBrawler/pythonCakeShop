import sqlite3 as sl
from random import randint
con = sl.connect('cake.db')
cur = con.cursor()
def createTableUsers():
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='users'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute("""
                        CREATE TABLE users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login VARCHAR(50),
                        password VARCHAR(50),
                        balance INTEGER NOT NULL,
                        card_id INTEGER NOT NULL,
                        FOREIGN KEY (card_id)
                        REFERENCES card (id)
                        );
                    """)
                    
def createTableAdmin():
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='admin'")
        for row in data:
            if row[0] == 0:
                with con:
                    con.execute("""
                        CREATE TABLE admin (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login VARCHAR(50),
                        password VARCHAR(50),
                        balance INTEGER
                        );
                    """)
                    sql = "INSERT INTO admin (login, password, balance) values(?, ?, ?)"
                    data = [("admin", "admin123",randint(20, 13000))]
                    with con:
                        con.executemany(sql, data)     


def createTableCake():
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='cake'")
        for row in data:
            if row[0] == 0:
                con.execute("""
                    CREATE TABLE cake (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ingredient_id INTEGER NOT NULL,
                    cake_num INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    cockroach INTEGER NOR NULL,
                    FOREIGN KEY (user_id)
                    REFERENCES user (id),
                    FOREIGN KEY (ingredient_id)
                    REFERENCES storage (id)
                    );
                """)

storageItemsList = ["flour",
                    "eggs",
                    "sugar",
                    "kefir",
                    "red_color",
                    "green_color",
                    "blue_color",
                    "cream_cheese",
                    "butter",
                    "oil",
                    "cream",
                    "strawberry",
                    "blueberry",
                    "rasberry",
                    "white_chocolate",
                    "milk_chocolate",
                    "dark_chocolate",
                    "vanilla",
                    "caramel",
                    "sugar_coat"]
def createTableStorage():
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='storage'")
        for row in data:
            if row[0] == 0:
                    con.execute("""
                        CREATE TABLE storage (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name_product VARCHAR(50) NOT NULL,
                        quantity_product INT NULL DEFAULT('-'),
                        price_product INTEGER NOT NULL
                        );
                    """)
                    for item in storageItemsList:
                        sql = "INSERT INTO storage (name_product, quantity_product, price_product) values(?, ?, ?)"
                        data = [(item, randint(1, 15), randint(20, 250))]
                        with con:
                            con.executemany(sql, data)  



cardList = [
    "Бронзовая карта",
    "Серебрянная карта",
    "Золотая карта"
]
cardDiscount = [
    5,
    10,
    20
]
def createTableCard():
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='card'")
        for row in data:
            if row[0] == 0:
                    con.execute("""
                        CREATE TABLE card (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name_card VARCHAR(50) NOT NULL,
                        discount INTEGER NOT NULL
                        );
                    """)
                    for i in range(3):
                        sql = "INSERT INTO card (name_card, discount) values(?, ?)"
                        data = [(cardList[i], cardDiscount[i])]
                        with con:
                            con.executemany(sql, data)
createTableUsers()
createTableAdmin()
createTableCake()
createTableStorage()
createTableCard()


