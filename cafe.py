import sqlite3 as sl
from random import randint
from databaseConfig import *  
from loginConfig import *
from adminPanel import *
from userPanel import *

def buyCake():
   with con:
       print("Сколько тортов вы хотите купить?")
       count = int(input())
       print("Доступные ингредиенты:")
       data = cur.execute("SELECT name_product FROM storage")
       row = data.fetchall()
       n = 0
       cockroach = randint(1,6)
       userFinds = randint(1,6)
       total = 0
       cake = 1
       while cake <= count:
            value = randint(10,1000)
            n = 0
            while n < 20:
                for i in row[n]:
                    print(f"Хотите добавить {i}? 1) Да, 2) Нет")
                    answer = int(input())
                    if (answer == 1):
                        with con:
                             
                            if (total  >= getUserBalance(getUserId(login))):
                                print("Вы больше не можете покупать так как недостаточно средств")
                                
                            else:
                                cur.execute("Select quantity_product from storage where id=?",(getIngredientId(str(i)),))
                                for rows in cur.fetchall():
                                    print(rows[0])
                                    if (int(rows[0]) > 0):
                                        cur.execute("select price_product from storage where id =?",(getIngredientId(str(i)),))
                                        for r in cur.fetchall():
                                            int(r[0])
                                        total += int(r[0]) 
                                        print(f"Вы добавили {i}")
                                        cur.execute("INSERT INTO cake (ingredient_id, cake_num, user_id, cockroach) values(?, ?, ?, ?)",(getIngredientId(str(i)),value,getUserId(login),cockroach,))
                                        cur.execute("update storage set quantity_product = quantity_product - 1 where id=?",(getIngredientId(str(i)),))
                                        con.commit()
                                        n += 1
                                    else:
                                        print("Данный ингредиент закончился")
                        
                    elif (answer == 2):
                        print(f"Вы не добавили {i}")
                        n += 1
            cake += 1
        
       cur.execute("Select card_id from users where id=?",(getUserId(login),))
       for r in cur.fetchall():
            if (int(r[0]) == 1):
                total = total - (5.0 * total / 100.0)
            elif (int(r[0]) == 2):
                total = total - (10.0 * total / 100.0)
            elif (int(r[0]) == 3):
                total = total - (20.0 * total / 100.0)
            if (cockroach == 5 and userFinds == 5):
                total = total - (30.0 * total / 100.0)

       cur.execute("update users set balance=? where id=?",((getUserBalance(getUserId(login)) - total),getUserId(login),))
       with con:
            cur.execute("SELECT name_product, cake_num, price_product FROM cake inner join storage on ingredient_id = storage.id where user_id =? and cake_num = ?",(getUserId(login),value))
            row = cur.fetchall()
       with open("cheque.txt", "w") as f:
            for item in row:
                f.write(item[0] + ".......") 
                f.write(str(item[2]))
                f.write("\n")
            if (cockroach == 5):
                f.write("Cockroach") 
                f.write("\n") 
            f.write(str(total))  


count = int(input())

match count:
    case 1:
        login = logIn()
        while(True):
            if (login == "admin"):
                print(f"Добро пожаловать {login}. Что вы хотите сделать?: \n 1) Пополнить склад \n 2) Изменить цену \n 3) Просмотреть историю покупок пользователя \n 4) Вывести баланс")

                count = int(input())
                
                match count:
                    case 1:
                        showAllProducts()
                        print("Введите id продукта")
                        id = int(input())
                        print("Введите количество продукта")
                        quantity = int(input())
                        updateQuantity(id,quantity)
                    case 2:
                        showAllProducts()
                        print("Введите id продукта")
                        id = int(input())
                        print("Введите новую цену продукта")
                        price = int(input())
                        updatePrice(id,price)
                    case 3:
                        print("Введите логин пользователя")
                        loginUser = input()
                        showUserHistory(getUserId(loginUser))
                    case 4:
                        print(getAdminBalance(1))
                       
            else:
                with con:
                        cur.execute("update users set balance = balance + ? where id=?",(randint(200,400),getUserId(login),))
                        con.commit()
                while(True):
                    if (login != False):
                        print(f"Добро пожаловать {login}. Что вы хотите сделать?: \n 1) Купить торт \n 2) Просмотреть историю покупок \n 3) Вывести общую сумму расходов \n 4) Вывести баланс")
                        
                        count = int(input())
                        
                        match count:
                            case 1:
                                buyCake()
                            case 2:
                                showUserHistory(getUserId(login))
                                updateCardUser(getUserId(login))
                            case 3:
                                print(getUserSpendings(getUserId(login)))
                            case 4:
                                print(getUserBalance(getUserId(login)))
            
    case 2:
        register()
    case _:
        print("dsdsd")

