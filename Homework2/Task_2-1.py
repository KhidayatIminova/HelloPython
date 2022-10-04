# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import os         
os.system('cls')

def InputNumbers ():
    check_input = False
    while not check_input:
        try:
            input_number = float(input(f'Введите вещественное число: '))
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
    return input_number

number = InputNumbers()

def GetSum(number):
    sum = 0
    for i in str(number): # преобразуем в строку и перебираем элементы
        try:  
            sum += int(i) 
        except ValueError: # ошибкам преобразования в int ('-', '.' и и т.п. всему что не цифра) присваиваем значение 0
            i = 0
    return sum

print(f"Сумма цифр числа {number} = {GetSum(number)}")