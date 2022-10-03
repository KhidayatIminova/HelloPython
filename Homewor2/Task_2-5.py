# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N,N]. 
# Найдите произведение элементов на указанных позициях (не индексах).

import os         
os.system('cls')
arr = []
def InputNumbers (arr):   
    check_input = False
    while not check_input:
        try:
            input_range = int(input('Введите размер диапазона: '))
            input_position1 = int(input('Введите номер позиции первого элемента: '))
            input_position2 = int(input('Введите номер позиции второго элемента: '))
            check_input = True 
            arr = [input_range, input_position1, input_position2]
            arr.append()           
        except ValueError:
            print ('Может еще раз? ')
    
    # list = [1,2,3]
    return arr
InputNumbers(arr)
print(arr)

ran = range(-arr[1],arr[1] + 1)
print(type(ran))
numbers = list(ran)
print(type(numbers))
print(numbers)
# print(numbers[0])
print (list)
print (numbers[arr[1] + 1])
print (numbers[arr[2] + 1])
mult = (numbers[arr[1] + 1] * numbers[arr[2] + 1])