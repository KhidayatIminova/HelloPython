# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os         
os.system('cls')

def InputNumber ():   
    check_input = False
    while not check_input:
        try:
            input_number = int(input('С точностью до какого знака хотим считать? (введите целое число): '))
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
    return input_number

n = abs(InputNumber())
d = 1 / (10**n)

print (f'Задана точность d = ', d)
print(f'π =', float(round(103993/33102, n))) # для оценки числа pi воспользуемся одним из рациональных приближений (103993/33102)

