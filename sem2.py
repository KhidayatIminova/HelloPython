from operator import truediv
import os         # библиотека os подключает команды, которые есть обычном виндовом терминале
os.system('cls')  # очистка терминала

# Защита от дурака

def InputNumbers (inputText):
    check_input = False
    while not check_input:
        try:
            number = int(input(f'{inputText}'))
            check_input = True
        except ValueError:
            print ('Введите корректные данные')
    return number

# day = InputNumbers('Введите цифру, обозначающую день недели: ')

# print (day)

# # Защита от дурака 2

# day = input(f'Введите цифру, обозначающую день недели')

# while not day.isdigit() and day not in ('1', '2', '3', '4', '5', '6', '7'): # или and day not in range (1,8)
#     day = input(f'Введите цифру, обозначающую день недели')
#     day = int(day)

# Или вот так:

# day = input(f'Введите цифру, обозначающую день недели')

# while day not in ('1', '2', '3', '4', '5', '6', '7'): # или and day not in range (1,8)
#     day = input(f'Нифига неверно! Говорю ж, введите ЦИФРУ, обозначающую день недели')
# day = int(day)



# n = '-123'

# minus = False
# if n[0] == '-':
#     minus = True
#     n = [1:] # используем срез по нулевому элементу (убираем минус)


# import random

# n = int(input('Введите любое целое число: '))

# for i in range(n):
#     print(random.randrange(0, n))

# from random import randint

import random as rd
for _ in range(10):
    print (rd.randint(-100,100))