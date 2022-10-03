# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

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

# k = int(round(((1 + 1/n)**n),0))
# # for i in range (1, k + 1):
    
#     # i = i + 1
# ran = range(1, k)
# numbers = list(ran)

# # numbers = list(ran)
# print(numbers)

array = []
i = 1
for i in range (n + 1):
    z = round(((1 + 1/i)**i),0)
    array.append(z)

print(array)