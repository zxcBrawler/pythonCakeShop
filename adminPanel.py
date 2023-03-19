import sqlite3 as sl
from random import randint
from databaseConfig import *  
from loginConfig import *




def showAllProducts():
     with con:
          data = con.execute("SELECT * FROM storage")
          row = data.fetchall()
          for item in row:
               print(item)

def getProductByID(id):
      with con:
          cur.execute("SELECT quantity_product FROM storage WHERE id=?", id)
          for row in cur.fetchall():
               print(row)

def updateQuantity(id, quantity):
    with con:
        cur.execute("SELECT price_product FROM storage where id = ?", (id,))
        for item in cur.fetchall():
             int(item[0])
        cur.execute("update storage set quantity_product =? where id=?",(quantity, id))
        cur.execute("update admin set balance = balance - ?",(int(item[0]) * quantity,))
        con.commit()

def updatePrice(id, price):
      with con:
        cur.execute("update storage set price_product =? where id=?",(price, id))
        con.commit()
