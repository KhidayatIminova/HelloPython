# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import os         
os.system('cls')

def InputNumber ():   
    check_input = False
    while not check_input:
        try:
            input_number = int(input('Задайте натуральную степень k: '))
            check_zero = 1/input_number
            check_input = True
        except ValueError:
            print ('Может еще раз? ')
        except ZeroDivisionError:
            print ('У этого полинома нету членов! Еще разок? ')
    return input_number

k = abs(InputNumber()) # полином будет без отрицательных степеней

from random import randint
nums = [randint(0,100) for _ in range(k+1)] # количество коэффициентов = степень + 1
print (nums)

def GetPolynom(count, nums):

    left_side_pol = []
    for i in range (count+1):
        
        # Условия для создания элементов левой части полинома
        
        if i == 1:
            s = str(nums[i]) + '*x' # замена для 'x' в первой степени
        elif i == 0:
            s = str(nums[i]) # при 'x' в нулевой степени ничего не добавляем 
        else:
            s = str(nums[i]) + '*x^' + str(i)

        # Условия для заполнения списка с элементами полинома

        if nums[i] ==1:
            s= s.replace("1*x","x") # замена, если коэффициент равен единице в связке с иксом
            left_side_pol.append(s)
        elif nums[i] !=0:
            left_side_pol.append(s)
    
    left_side_pol.reverse() # реверс списка для отображения левой части полинома по нисходящей степени
    polynom = " + ".join(left_side_pol) + ' = 0' # добавляем правую часть

    return polynom
  
print(f'\n{GetPolynom(k, nums)}\n')

data = open('tsk4-4.txt', 'w') 
# data = open('tsk4-51.txt', 'w') 
# data = open('tsk4-52.txt', 'w') 
data.writelines(GetPolynom(k, nums)) 
data.close() 

