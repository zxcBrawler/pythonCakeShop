import sqlite3 as sl
from random import randint
from databaseConfig import *  
from loginConfig import *



def getUserId(login):
    with con:
        cur.execute("SELECT id FROM users WHERE login =?",(login,))
        for row in cur.fetchall():
            return int(row[0])
    
def getIngredientId(name_product):
    with con:
        cur.execute("SELECT id FROM storage WHERE name_product =?",(name_product,))
        for row in cur.fetchall():
            return int(row[0])

def showUserHistory(id):
   with con:
        cur.execute("select name_card from users inner join card on card_id = card.id where users.id = ?",(id,))
        for row in cur.fetchall():
               print(row[0])
        data = con.execute("SELECT group_concat(name_product,','), cake_num, sum(price_product) FROM cake inner join storage on ingredient_id = storage.id where user_id =? group by cake_num",(id,))
        row = data.fetchall()
        for item in row:
            print("Номер заказа: " + str(item[1]))
            print("Состав торта: " + str(item[0]))
            print("Итог : " + str(item[2]))

def getUserSpendings(id):
    with con:
        cur.execute("select sum(price_product) FROM cake inner join storage on ingredient_id = storage.id where user_id =? group by user_id",(id,))
        for row in cur.fetchall():
            return int(row[0])

def getUserBalance(id):
    with con:
        cur.execute("select balance from users where id =?",(id,))
        for row in cur.fetchall():
            return int(row[0])
def updateCardUser(id):
    if (int(getUserSpendings(id)) > 15000):
        cur.execute("update users set card_id = ? where id=?",(2,id,))
        con.commit()
    if (int(getUserSpendings(id)) > 20000):
        cur.execute("update users set card_id = ? where id=?",(3,id,))
        con.commit()

        



           

