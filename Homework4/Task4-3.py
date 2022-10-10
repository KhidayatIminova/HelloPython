# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os         
os.system('cls')

from random import randint
count = 10
nums = [randint(1,10) for _ in range(count)]
print (nums)

def UnrepeatedNums(arr):
    unrepeated=[] # в этом списке будут храниться неповторяющиеся числа
    for i in range (count):
            if arr.count(i) == 1: # если элемент встречается 1 раз
                unrepeated.append(i) # помещаем его в список unrepeated
    if len(unrepeated) == 0: # в случае отстутствия уникальных элементов - в unrepeated не запишется ничего, следовательно его длина будет = 0
        print('\nВ исходной последовательности неповторяющихся чисел нет\n')
    else:
        print(f'\nНеповторяющиеся числа: ', unrepeated, end='\n\n')

UnrepeatedNums(nums)