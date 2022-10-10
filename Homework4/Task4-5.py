# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

path1 = 'tsk4-51.txt'
path2 = 'tsk4-52.txt'
path_sum = 'tsk4-53.txt'

import os         
os.system('cls')


# def ReadData(path):
#     with open(str(path), 'r') as data:
#         pol = data.read()
#     return pol


# p1 = open(path1, 'r')
# print(p1)

# p2 = open(path2, 'r')
# print(p2)

p1 = '64*x^4 + 65*x^3 + 74*x^2 + 71*x + 18 = 0'
p2 = '34*x^3 + 36*x^2 + 92*x + 53 = 0'

print(len(p1))
print(len(p2))

p1 = p1.strip()
print(len(p1))
print(p1.count('^4'))


pol1 = p1.split()
pol1 = p1.replace('+','')
pol1 = pol1.replace('= 0','')
pol1 = pol1.replace('*',' ')
print(pol1)




