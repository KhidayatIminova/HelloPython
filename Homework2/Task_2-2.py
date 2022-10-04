# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os         
os.system('cls')

def InputNumbers ():    # Всё-таки "защита от дурака" с помощью try - except охватывает всё)
    check_input = False
    while not check_input:
        try:
            input_number = int(input('Введите целое число: '))
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
    return input_number

def GetFactorial(n):
    nfactorial = 1
    print (f'{n}! = ', sep=' ', end=' ')
    for i in range (1, n + 1):
        nfactorial = nfactorial * i
        i = i + 1
        print(f'{nfactorial}', sep=' ', end=' ')
    print()

GetFactorial(InputNumbers())