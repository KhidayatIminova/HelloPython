import model as md
import controller as con
import os
  
os.system('cls')
print('Добро пожаловать в БД...')

def input_int(msg=""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result

def main_menu():
    global finish
    db = con.open_db()
    print('Показать все записи справочника - 1')
    print('Добавить запись - 2')
    print('Удалить запись - 3')
    print('Изменить запись - 4')
    print('Найти запись - 5')
    print('Выход - 0')
    option = input_int('Введите номер операции: ')
    if option == 1:
        md.print_db(db)
        input("\nДля возврата в меню нажмите Enter")
    elif option == 2:
        md.add(db)
        input("\nДля возврата в меню нажмите Enter")
    elif option == 3:
        md.print_db(db)
        md.del_value(input_int("Введите номер записи для удаления: "))
        input("\nДля возврата в меню нажмите Enter")
    elif option == 4:
        md.edit_value()
        input("\nДля возврата в меню нажмите Enter")
    elif option == 5:
        md.find()
        input("\nДля возврата в меню нажмите Enter")
    elif option == 0:
        finish = True

finish = False
while not finish:
    main_menu()