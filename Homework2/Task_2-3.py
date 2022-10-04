# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

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

subsequence = []
sum = 0
for i in range (1, n + 1):
    z = int(round((1 + 1/i)**i,0))
    subsequence.append(z)
    sum = sum + z

print(f'{subsequence} -> {sum}')
