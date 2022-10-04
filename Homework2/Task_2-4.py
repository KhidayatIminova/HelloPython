# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 2. Реализуйте алгоритм перемешивания списка.# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N,N]. 
# Найдите произведение элементов на указанных позициях (не индексах).

# Position one 1
# Posotion two 3
# Number of elements 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

# Исходя из приведенного примера условие не совсем корректно: в промежутке [-N, N] существует (2*N + 1) элементов

import os         
os.system('cls')

def InputNumbers ():   
    check_input = False
    while not check_input:
        try:
            input_range = int(input('Введите число N для промежутка [-N, N]: '))
            print (f'Допустимый диапазон позиций от 1 до {2*input_range+1}')
            input_position1 = int(input('Введите номер позиции первого элемента: '))
            input_position2 = int(input('Введите номер позиции второго элемента: '))
            
            if (input_position2 > (2*input_range+1) or input_position1 > (2*input_range+1)):    # проверка соответствия позиций диапазону
                check_input = False
                print ('\nПозиции элементов вне допустимого диапазона. Попробуйте еще раз. \n')
            elif (input_position2 < 0 or input_position1 < 0):    # проверка на отрицательные позиции
                check_input = False
                print ('\nОтрицательных позиций не существует. Попробуйте еще раз. \n')
            else:
                check_input = True 
            arr = [input_range, input_position1, input_position2] # создадим промежуточный список входных данных         
        except ValueError:
            print ('Может еще раз? ')
    return arr

arr = InputNumbers()
# print(arr) # список входных данных

ran = range(-arr[0],arr[0] + 1)
numbers = list(ran)
print(numbers)

mult = (numbers[arr[1] - 1] * numbers[arr[2] - 1]) # позиция элемента в списке = (индекс + 1)
print (mult)
