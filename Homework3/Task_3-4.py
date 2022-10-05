# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os         
os.system('cls')

def InputNumber ():   
    check_input = False
    while not check_input:
        try:
            input_number = int(input('Введите целое число: '))
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
    return input_number

n = InputNumber() 

def GetBinNumber(num):
    
    number = abs(num) # чтобы метод не сломался от отрицательного числа
    n_bin = '' # строковая переменная для хранения остатков от деления

    while number>0:
        fraction = str(number%2) # остаток для каждой итерации (для наглядности)
        n_bin = fraction + n_bin # добавление остатка в строку
        # n_bin = str(number%2) + n_bin # можно без fraction 
        print (f'\n{number}/2 = {number // 2} + остаток {fraction} --> {n_bin}')
        number = number // 2
    print()

GetBinNumber(n)
