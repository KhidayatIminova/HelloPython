# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

check_type = 0
try:
    x = float(input('Введите координату х: '))
    y = float(input('Введите координату y: '))
except ValueError:
    check_type = 1

def check_quadrant(x,y):
       
    if x > 0 and y > 0:
        quad = 1
    elif x < 0 and y > 0:
        quad = 2
    elif x < 0 and y < 0:
        quad = 3
    else:
        quad = 4
    return (quad)

if check_type == 0 and x != y != 0:
    print(f"Точка с координатами [{x}; {y}] находится в {check_quadrant(x,y)}-й четверти")
elif check_type == 1:
    print ('\nАйяйяй! Координата должна быть числом!\n')
else:
    print(f"Точка с координатами [{x}; {y}] является началом координат")


