# print ('hello')

# # Типы переменных
# # int, float, boolean, str, list, None

# # C#:   int a; 
# # В Python просто a = 123 (int), b = 1.23 (float), 

# value = None
# print(type(value))
# a = 123
# b = 1.23

# print(a)
# print(type(a))
# print(b)
# print(type(b))
# # для того, чтобы переменную использовать дальше по коду value = None
# value = 12345
# print (value)
# print(type(value))

# s = 'hello \nworld'

# print(s)
# # Способы вывода
# print (a, ' - ',b, ' +++ ',s, ' bebebe ')
# print ('{} -- {} +++ {} bububu'.format(a, b, s))
# print ('{2} -- {0} +++ {1} bububu'.format(a, b, s)) #изменение порядка вывода переменных
# print (f'{a} /*/ {b} *** {s} bababa')

# f = True # логическая переменная
# g = False
# print(f, g)


# Списки

# # В C# явно выделены массивы. В Pythone как таковых массивов нет. Массивы заменяют списки
# # Для того, чтобы объявить что-то похожее на массив:

# list = [1,2,3] # список целочисленных данных
# print(type(list))
# print (list)

# list = ['1','2','3','hello'] # список строковых данных
# print (list)

# # Поскольку у языка Python динамическая типизация, можно миксовать различные типы в одном списке

# list = ['1','2','3','hello', 1,2,3,4.5,True] # список комбинированных данных (но так делать не нужно)
# print (list)

# # Пробел может поломать программу!!!

# # Ввод и вывод данных

# # print () отвечает за вывод данных
# # input () отвечает за ввод данных

# print ('Input a:')
# a = input ()
# print ('Input b:')
# b = input ()
# print (a, b)
# print ('{}, {}'.format(a,b))
# print (f'{a} {b}')
# print (a + b) # по умолчанию работаем со строками, поэтому в данном случае 10 + 20 будет 1020

# # для выполнения арифметических действий необходимо определить тип перед input
# a = int(input()) # целочисленное значение
# b = float(input()) # вещественное значение
# print (a + b)

# # Арифметические операции
# # +, -, *, /, %, **, //
# # **, , , 
# # () Сокращенные операции

# a = 123
# b = 321
# c=a+b
# print(c)

# a = +123 # унарный плюс
# b = -321 # унарный минус
# c=a+b
# print(c)

# a = 4.512346
# b = 3 
# c=a/b # операция деления работает как для вещественных чисел
# print(c)
# c=a//b # результат будет целым числом
# print(c)
# c=a % b # результат будет остаток от деления (не десятичный - например 20/8 = 2 целых, 4 в остатке - результат 4)
# print(c)
# c=a**b # возведение в степень (a в степени b). При этом нет ограничения по объему памяти
# print(c)

# print(c)
# c=round(a*b, 5) # при умножении вещественных чисел результат может быть некорректен (особенности хранения вещ.чисел). Используем round - округление по математическим правилам
# print(c)

# # Сокращенные операции присваивания

# a = 8
# a +=5 # a = a + 5 аналогичным образом для других арифметических операций
# print (a)

# # Логические операции

# # >, >=, <, <=, ==, !=
# #  not, and, or - не путать с &, |, ^
# # is, is not, in, not in
# # gen

# a = 1 > 4
# print (a) # на выходе результат будет False

# a = 1 < 4 and 5 > 2
# print (a) # на выходе результат будет True

# a = 'qwe'
# b = 'qwe'
# print (a == b) # сравнение строк, результат будет True

# a = [1,2]
# b = [1,2]
# print (a == b) # сравнение списков (поэлементное), результат будет True

# a = 1 < 4 < 5 < 10 # в Python можно использовать тройные и четверные неравенства
# print (a) # на выходе результат будет True

# func = 1
# T = 4
# x = 123

# print (func<T>x)

# f = 1 > 2 or 4 < 6
# print (f)

# f = [1, 2, 3, 4]
# print (f)
# print (2 in f) # высказывание "2 есть в списке f" результат True, т.к. двойка в списке есть
# print (not 2 in f) # высказывание "2 нет в списке f" результат False, т.к. двойка в списке есть

# # проверка на четность
# is_odd = f[0] % 2 == 0 # остаток от деления нулевого элемента списка f на 2 равен 0?
# print (is_odd)

# # По-умолчанию в пайтоне мы также считаем, что 0 это ложь, а 1 истина. Технически можно записать так:
# is_odd = not f[0] % 2 # то же самое, но по-пайтоновски. У нечетного числа при делении на 2 остаток всегда будет 1. В данном случае результат деления 1, отрицание 1 это 0, 0 это False.
# print (is_odd)

# Управляющие конструкции
# if, if-else

# ОТСТУПЫ ВАЖНЫ!!!

# a = int(input())
# b = int(input())
# if a > b:
#     print (a)
# else:
#     print (b)

# username = input ('Введите имя: ')
# if username == 'Маша':
#     print ('Ура, это же Маша!')
# elif username == 'Марина':
#     print ('Это Марина!')
# else:
#     print ('Привет', username)

# Управляющие конструкции: While

# # Перевернутое число
# original = 23
# invertered = 0 # присваиваем первичное значение 0
# while original !=0: # пока не равно нулю
#     invertered = invertered*10 + (original%10) # делим на 10 и прибавляем остаток (в результате должен остаться остаток 3)
#     # print('i =', invertered)  # цикл пошагово
#     original //=10
#     # print('o =', original) # цикл пошагово
# else:
#     print('Пожалуй')
#     print('хватит')
# print('invertered =',invertered)

# цикл For

# for i in 1,2,3,4,5:
#     print (i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print (i**2)

# r = range(10) # в диапазоне [0,10)
# for i in r:
#     print (i)

# r = range(1, 5) # в диапазоне [1, 5)
# for i in r:
#     print (i)

# r = range(1, 5, 2) # в диапазоне [1, 5) с приращением 2
# for i in r:
#     print (i)

# for i in 'qwerty': # перебор букв в строке
#     print (i)

# Строки

text = 'cъешь еще этих мягких французских булок'
# print(len(text)) # длина строки 39
# print('еще' in text)  # True наличие
# print(text.isdigit()) # False символы являются числами
# print(text.islower()) # True нижний регистр
# print(text.replace('еще', 'ЕЩЕ')) # замена

# for с in text:
#     print (с)

# help(text.istitle) # покажет что делает text.istitle

# # Срезы

# # Представляем строку как некий массив символов. Можно обращаться к конкретному элементу строки через его индекс

# print(text[0]) # с
# # print(text[len(text)]) # Index Error
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # 
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь еще
# print(text[6:-18]) # еще этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] #...

# Списки

# numbers = [1,2,3,4,5]
# print (numbers) # [1,2,3,4,5]

# ran = range(1,6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)  # 1,2,3,4,5

# numbers [0] = 10
# print(f'{len(numbers)} len')
# print (numbers) # 10,2,3,4,5

# for i in numbers:
#     i *=2
#     print (i)   # [20,4,6,8,10]
# print (numbers) # [10,2,3,4,5]


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)    # red green blue

# for e in colors:
#     print(e*2)    # redred greengreen blueblue

# colors.append('grey')   # добавить в конец
# print (colors == ['red', 'green', 'blue', 'grey'])  # True
# print (colors)  # ['red', 'green', 'blue', 'grey']
# colors.remove('red') # или del colors[0] - удалить элемент
# del colors[0]
# print (colors)  # ['blue', 'grey']

# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print (f(arg))
print (type(f(arg))) # 'str'

arg = 2.3
print (f(arg))
print (type(f(arg))) # 'int'

arg = 2
print (f(arg))
print (type(f(arg))) # 'NoneType'