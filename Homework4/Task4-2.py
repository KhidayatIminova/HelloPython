# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

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

n = abs(InputNumber()) # модуль на случай ввода отрицательного числа 

def GetNumberFactor(n):
    arr = []
    for i in range (1,10):
        if not n%i: # если заданное число n делится на множитель i нацело
            # print(f'{i} является множителем числа {n}')
            arr.append(i)
    return arr

print(f'\nПростыми множителями натурального числа {n} являются числа', GetNumberFactor(n), end='\n\n')
