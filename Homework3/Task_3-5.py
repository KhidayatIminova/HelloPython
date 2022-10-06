# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os         
os.system('cls')

def InputNumber ():   
    check_input = False
    while not check_input:
        try:
            input_number = int(input('Введите целое число k: '))
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
    return input_number

k = abs(InputNumber()) # чтобы скрипт не сломался от отрицательного числа

def fib(n):
# для отрицательного диапазона    

            if n == -1:
                return 1
            elif n == -2:
                return -1

            elif n < 0:
               
                fib(n+2) - fib(n+1)
                return fib(n+2) - fib(n+1)

# для положительного диапазона   
         
            elif n in [1, 2]:
                return 1
            # elif n == 0: # можно добавить условие нулевого элемента чтобы не пересчитывал
            #     return 0
            else:       
                return fib(n-1) + fib(n-2)
            
list = []
for e in range (-k, k+1):
    list.append(fib(e))     
print(list)

