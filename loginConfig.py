from databaseConfig import * 
from loginConfig import * 
print("1 - Вход\n2 - Регистрация")


def logIn():
    print("Вход в аккаунт")
    print("Введите логин")
    login = input()
    print("Введите пароль")
    passwd = input()
    with con:
        data = con.execute(f"select count(*) from users where login='{login}' and password='{passwd}'")
        for row in data:
            if row[0] != 0:
                print("Успешный вход")
                return login
              
                
            elif row[0] == 0 :
                data = con.execute(f"select count(*) from admin where login='{login}' and password='{passwd}'")
                for row in data:
                    if row[0] != 0:
                        print("Успешный вход админ")
                        return login
                    else:
                        print("Неправильный логин или пароль")
                        return False

def register():
    print("Регистрация")
    print("Введите логин")
    login = input()
    print("Введите пароль")
    passwd = input()
    with con:
        data = con.execute(f"select count(*) from users where login='{login}' and password='{passwd}'")
        for row in data:
            if row[0] != 0:
                print("Данный пользователь уже существует")
        else:
            sql = "INSERT INTO users (login, password, balance,card_id) values(?, ?, ?, ?)"
            data = [(login, passwd, randint(20, 1300), 1)]
            with con:
                con.executemany(sql, data)     