# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant = (input('Введите номер четверти (1 - 4): '))

def Get_points_range (q_number):
  
    if q_number == '1':
        print (f'Диапазон возможных координат 1-й четверти: (x > 0; y > 0)')
    elif q_number == '2':
        print (f'Диапазон возможных координат 2-й четверти: (x < 0; y > 0)')
    elif q_number == '3':
        print (f'Диапазон возможных координат 3-й четверти: (x < 0; y < 0)')
    elif q_number == '4':
        print (f'Диапазон возможных координат 4-й четверти: (x > 0; y < 0)')
    else:
        print('\nНомер какой-то неправильный...или это вообще не номер\n')

Get_points_range (quadrant)
