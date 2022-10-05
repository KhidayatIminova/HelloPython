# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os         
os.system('cls')

from random import randint
count = 10
nums = [randint(1,20) for i in range(count)]
print (nums)

def PairMultiply(arr):
    for i in range(int(len(arr)/2)): #  в случае нечетного количества элементов исключаем из расчета средний элемент
        mult = arr[i] * arr[len(arr)-1-i]
        print (f'A[{i}] * A[{len(arr)-1-i}] = {arr[i]} * {arr[len(arr)-1-i]} = {mult}')

PairMultiply(nums)
