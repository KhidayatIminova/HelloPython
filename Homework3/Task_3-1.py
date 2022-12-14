# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os         
os.system('cls')

from random import randint
count = 10
nums = [randint(1,20) for _ in range(count)]
print (nums)

sum = 0
print (f'Элементы с нечетными индексами: ', end=' ' ) # исходя из приведенного в условии примера принимаем что позиция = индекс
for i in range(1, len(nums), 2):  # начинаем с индекса 1 с приращением 2
    
    sum = sum + nums[i]
    
    print (f'{nums[i]}', end=' ' )
print (f'\nСумма элементов с нечетными индексами = {sum}')