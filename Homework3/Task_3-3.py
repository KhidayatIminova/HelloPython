# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os         
os.system('cls')

from random import randint
count = 10
nums = [randint(1,20)/1000 + randint(1,20) for i in range(count)]
print (nums)

def GetMinMaxDifferent(arr):

    fraction_max = 0
    fraction_min = 1

    for i in range(len(arr)):

        if (nums[i]-int(nums[i]))>fraction_max: # сравним дробную часть с максимальным значением
            fraction_max = round(nums[i]-int(nums[i]),3)

        if ((nums[i]-int(nums[i])))<fraction_min: # # сравним дробную часть с минимальным значением
            fraction_min = round(nums[i]-int(nums[i]),3)

    print ('\nМаксимальное значение дробной части = ', fraction_max, '\nМинимальное значение дробной части = ', fraction_min)
    print ('\nРазница между максимальным и минимальным значением дробной части элементов = ', round(fraction_max - fraction_min, 3),'\n')

GetMinMaxDifferent(nums)