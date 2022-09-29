# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# a = (input('Введите x: '))
# y = (input('Введите y: '))

# print (a.isnumeric())
# print (a.isdecimal())
# print (a.isdigit())
# if a.isdigit() == True and float (a) != 0 and y.isdigit() == True and float (y) != 0:
#     print ('[', a, ' , ', y, '] ')
# else:
#     print('Правильна цыфры тыкай!!')


k = []
for i in range (2):
    z = (input('Введите число: '))
    k.append(z)

print(k)

# print (k.isnumeric())
# print (k.isdecimal())
# print (k.isdigit())

print(type(k[0]))
print(type(k[1]))