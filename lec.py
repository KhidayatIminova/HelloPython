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

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print (f(arg))
# print (type(f(arg))) # 'str'

# arg = 2.3
# print (f(arg))
# print (type(f(arg))) # 'int'

# arg = 2
# print (f(arg))
# print (type(f(arg))) # 'NoneType'



#####################################

# STEPIK

# Параметр sep

# Рассмотрим следующий код: 

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**')
# Результатом выполнения такого кода будет:

# a*b*c
# d**e**f

# Параметр end
# Если перевод строки делать не нужно или требуется указать специальное окончание, то следует явно указать значение для параметра end.

# # Рассмотрим следующий код:

# print('a', 'b', 'c', end='@')
# print('d', 'e', 'f', end='@@')
# # Результатом выполнения такого кода будет:

# # a b c@d e f@@

# Параметры sep и end можно использовать вместе. Рассмотрим следующий код:

# print('a', 'b', 'c', sep='*', end='finish')
# print('d', 'e', 'f', sep='**', end='^__^')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='#')
# print('m', 'n', 'o', sep='/', end='!')
# Результатом выполнения такого кода будет:

# a*b*cfinishd**e**f^__^g+h+i%j-k-l#m/n/o!

# Примечание 3. Значения по умолчанию у параметров sep и end следующие:

# sep=' '   # пробел
# end='\n'  # перевод строки
# Примечание 4. Чтобы убрать все дополнительные выводимые символы, можно вызывать командуprint() так:

# print('a', 'b', 'c', sep='', end='')

# Множественное присваивание
# В языке Python можно за одну инструкцию присваивания изменять значение сразу нескольких переменных. Делается это так:

# name, surname = 'Timur', 'Guev'
# print('Имя:', name, 'Фамилия:', surname)

# Если требуется считать текст с клавиатуры и присвоить его в качестве значения переменным, то можно написать так: 

# name, surname = input(), input()
# print('Имя:', name, 'Фамилия:', surname)

# Множественное присваивание удобно использовать, когда нужно обменять значения двух переменных. В Python это делается так:

# name1 = 'Timur'
# name2 = 'Gvido'
# name1, name2 = name2, name1

# При оформлении программ мы будем пользоваться PEP 8 — Python Enhanced Proposal.

# Рекомендация 1. Избегайте использования пробелов перед открывающей скобкой, после которой начинается список аргументов функции.

# Правильно:

# print('Follow PEP8!')
# Неправильно:

# print ('Follow PEP8!')
# Рекомендация 2. После запятой нужен пробел.

# Правильно:

# print('PEP8', 'Rocks!')
# Неправильно:

# print('PEP8','Rocks!')
###
# Рекомендация 3. Не отделяйте пробелами знак «равно», когда он употребляется для обозначения значения параметра по умолчанию.

# Правильно:

# print('My name', 'is', 'Python', sep='**', end='+')
# Неправильно:

# # print('My name', 'is', 'Python', sep = '**', end = '+')
###

# При делении отрицательных чисел необходимо помнить, что результат целочисленного деления не превосходит частное. Другими словами, округление берётся в меньшую сторону (число -4−4 меньше, чем число -3−3).

# Результатом работы следующей программы:

# print(10 // 3)
# print(-10 // 3)
# будут числа:

# 3   # округление в меньшую сторону
# -4  # округление в меньшую сторону

#  Примечание 5. Обратите внимание: результатом деления n % m при n < m является число n. Например, 5 % 9 = 5, 3 % 13 = 3 и т.д.

# print(1 % 3)

# print(2//5)


# лекция 2 Работа с файлами

# a - открытие и добавление данных
# r - открытие для чтения данных
# w - открытие для записи данных
# r+, w+




# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # открыть чтобы добавить данные (если w, то данные перезапишутся)
# data.writelines(colors) # добавляем данные colors (разделителей не будет)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close() # обязательно вызвать закрытие файла (разрыв связи с data)

# Второй способ

# with open('file.txt', 'a') as data: # воспринимать эту конструкцию как переменную data
#     data.write('LINE 1\n')
#     data.write('LINE 2\n')

# В данном случае разрыв связи data с file.txt будет автоматическим

# exit() # позволяет не выполнять дальше код скрипта

# чтение данных из файла

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Функции и модули

# import sem2 # импортировать из файла sem2.py

# print(sem2.InputNumbers('проверка импорта')) # метод InputNumbers с параметром InputText = 'проверка импорта'

# # можно сделать альяс, если лень писать

# import sem2 as s2 # sem2 придумаем псевдоним s2

# print(s2.InputNumbers('проверка импорта'))

# # Таким образом, программу можно разделить на файлы скриптов, которые можно выдергивать импортом

# Функции

# def new_string(symbol, count):
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# # можно вот так:

# def new_string(symbol, count=3): # по умолчанию делаем count = 3
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!! - используется count = 3 по умолчанию
# print(new_string(4)) # 12 - то же самое, используется count = 3 по умолчанию

# функция с неограниченным набором параметров

# def concatenatio(*params): # *param - неограниченный набор параметров
#     res: str = ''
#     for item in params:
#         res += item
#     return res

# print (concatenatio('a', 's', 'd', 'w')) # asdw
# print (concatenatio('a', '1')) # a1
# print (concatenatio(1, 2, 3, 4)) # TypeError ...

# Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range (1,10):
#     list.append(fib(e))     
# print(list)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Кортежи

# a, b = 3, 4 # множественное присваивание

# (a) = (3, 1, 2, 4) # кортеж
# print(a)
# print(a[0]) # обращение к конкретному элементу

# print(a[-1]) # обращение к последнему элементу (по аналогии со списками)

# # кортеж это неизменяемый "список"

# t = ()
# print(type(t)) # tuple
# t = (1,) # для определения кортежа из одного элемента необходима запятая, иначе определится как число
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # red green blue
# t=tuple(colors) 
# print(t) # red green blue
# t[0] = 'black' # TypeError... кортеж - неизменяемый "список"

# перебор кортежа

# a = (3, 4, 5)

# for item in a:
#     print(item) 

# Можно распаковать кортеж в отдельные переменные через двойное преобразование

# t = tuple(['red', 'green', 'blue']) # создаем список, конвертируем его в кортеж

# red, green, blue = t # дальше кортежраспаковываем, превращаем его в три независимых переменных
# # далее уже с ними работаем как с отдельными переменными
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r: red g: green b: blue 

# Словари

# это неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {} # пустой словарь

# чтобы не писать всё в одну строчку используется \

# dictionary = \
#     {
#         'up': '^', # ключ 'up', значение по ключу '^'
#         'down': 'v',
#         'left': '<',
#         'right': '>' 
#     }
# print(dictionary) # {'up': '^','down': 'v','left': '<','right': '>'}
# print(dictionary['left']) # < (для словаря указывается не индекс, а то значение, которое определили при описании)

# типы ключей могут отличаться

# for k in dictionary.keys(): # все ключи
#     print (k)


# for k in dictionary.values(): # все значения
#     print (k)

# # или так:

# for k in dictionary: 
#     print (k) # все ключи

# for k in dictionary: 
#     print (dictionary[k]) # все значения

# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# вывод парами

# for item in dictionary: # for (k,v) in dictionary.item():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ^
# # down: v
# # left: <
# # right: >

# print(dictionary['up'])
# dictionary['up'] = 'Upper'
# print(dictionary['up'])

# Множества

# colors = {'red', 'green', 'blue'} # заменим квадратные скобки [] на {}
# print(type(colors)) # set - тип данных множество
# print(colors) # {'red', 'green', 'blue'}

# colors.add('red') # добавить. В данном случае red уже есть, ошибок не будет, но и добавления не будет
# print(colors) # {'green', 'blue', 'red'} # происходит смещение элементов - почему? (незакомментировал код распаковки через двойное преобразование см.выше)
# colors.add('gray')
# print(colors) # {'gray', 'green', 'blue', 'red'}
# colors.remove('red')
# print(colors) # {'gray', 'green', 'blue'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok исключить элемент?
# print(colors) # {'gray', 'green', 'blue', 'red'}
# colors.clear() # {}
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}

# # Неизменяемые множества

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# #{1, 21, 3, 13}

# s = frozenset(a) # заморозка множества - никакие методы удаления/ добавления работать не будут


# Списки (углубленно)

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# list1[0] = 123 # также меняется значение и во втором списке
# list2[1] = 333 # также меняется значение и в первом списке

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# print(list1.pop())



# Лекция 3

# Анонимные, lambda функции

# Добустим есть несколько функций, которые могут понадобиться

# def sum(x):
#     return x+10

# def mult(x):
#     return x**2

# def sum1(x):
#     return x+22

# допустим они могут понадобиться в программе 1 раз. Каким образом можно обойтись без явного описания:

# # допустим есть некая функция

# def f(x):
#     return x**2

# # у функции есть имя, следовательно есть тип

# print(type(f)) # class 'function'

# g = f # присвоим переменной g значение f (т.е. в переменную положим функцию целиком)

# # теперь можно вызвать как f(), так и g() и работать это будет одинаково (логично))

# print(f(1))
# print(g(1))

# # также будут совпадать типы
# print(type(g))
# # т.е. в контексте приложения есть переменная, которая хранит в себе функцию

# def calc1(x):
#     return x+10
# print(calc1(10))

# def calc2(x):
#     return x**2
# print(calc2(10))

# # в идеале чтобы не плодить однотипные функции, нужно просто взять некую функцию calc, которая будет выполнять арифметическую операцию

# # возьмем некую функцию math, где в качестве аргумета будет приходить какая-то операция, и соответственно какое-то число 

# def math(op,x): # т.е. в функции аргументом выступает другая функция
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# calc(mult, 4, 5)

# Лямбда - чтобы было красиво

# def sum(x, y):
#     return x+y
# # f = sum # можно вот так

# sum = lambda x, y: x+y # или вот так, что будет аналогично записи def sum()

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     # return op(a,b)

# # # calc(f, 4, 5)
# # calc(sum, 4, 5)

# #№ Или можно вообще пробросить лямбду сразу:

# calc(lambda x, y: x+y, 4, 5)

# List Comprehensions

# Допустим хотим создать список из чётных чисел в диапазоне от 1 до 100

# list=[]

# for i in range(1, 101):
#     if (i%2 == 0):
#         list.append(i)
# print(list)

# list = [i for i in range(1,101)] # аналогичная запись в одну строку (для вывода четных и нечетных)
# print(list)

# list = [i for i in range(1,21) if i%2 == 0] # если остаток от деления на 2 равен 0
# print(list)


# def f(x):
#     return x**3

# list = [f(i) for i in range(1,21) if i%2 == 0] # то же самое для функции
# print(list)

# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1,21) if i%2 == 0] # то же самое для пар число и его куб
# print(list)

# # Задача: в файле file.txt записан ряд чисел 1 2 3 5 8 13 23 38. Считать из файла, вывести пары число и его квадрат

# path = 'C:/Users/ПК/Desktop/Education/PYTHON/file.txt'
# f = open(path, 'r')
# data = f.read() + ' ' # приём: считать всё, что есть в файле и добавить пробел
# f.close

# print(data)

# numbers = [] # создаем пустой список

# while data != '': # пока строка не пустая
#     space_pos = data.index(' ') # находим первую позицию пробела
#     numbers.append(int(data[:space_pos])) # взять всё, что находится от первого символа до позиции первого пробела, превратить это в число и добавить в список чисел
#     data = data[space_pos + 1:] # обновить строку с учетом добавления

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e,e**2)) # список кортежей число и его квадрат

# print (out)       

# # то же через лямбда

# def select(f, col): # опишем некоторую функцию select, которая будет принимать какую-то функцию и какой-то набор данных
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 13 23 38'.split()

# res = select(int, data) # в качестве первого аргумента функция int, которая отвечает за преобразование строк в число

# print(res) # на выходе получаем список чисел

# res = where(lambda x: not x%2, res ) # в качестве первого аргумента описываем лямбда функцию для чётных чисел

# print(res)

# res = select(lambda x: (x, x**2), res ) # в качестве первого аргумента описываем лямбда функцию для кортежей число и его квадрат

# print(res)

# Функция map

# li = [x for x in range(1,20)]

# # хотим получить новый набор данных через функцию map

# # li = map(lambda x: x + 10, li) # в качестве первого аргумента передадим лямбда, увеличивающую х на 10, в качестве второго сам набор данных - ошибка map object
# li = list(map(lambda x: x + 10, li)) # делаем явное преобразование в список



# print(li)


# Допустим есть набор данных, получаемый с клавиатуры

# data = input().split() # вводим и сразу разбиваем, в качестве разделителя пробел
# data = input().split(',') # вводим и сразу разбиваем, в качестве разделителя запятая

# data = list(map(int,input().split())) # пробрасываем в map: в качестве первого аргумента функция int

# print(data)

## Без явного преобразования в list:

# data = map(int,'1 2 345 65 4 77'.split()) # уже готовая строка, парсим ее на числа

# for e in data:
#     print(e)

# print('---')

# # итак, есть объект map, продублируем вывод еще раз

# for e in data:
#     print(e) # и получаем - ничего, т.к. результат работы map это некий итератор, по итератору можно пробужаться только один раз,
#     #  поэтому длшя дальнейшей работы их нужно принудительно сохранять, например в списке (или явным преобразованием)

## теперь применим map вместо ранее описанной select

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 13 23 38'.split()

# res = map(int, data) # в качестве первого аргумента функция int, которая отвечает за преобразование строк в число

# # print(res) # на выходе получаем список чисел

# res = where(lambda x: not x%2, res ) # в качестве первого аргумента описываем лямбда функцию для чётных чисел

# # print(res)

# res = list(map(lambda x: (x, x**2), res )) # в качестве первого аргумента описываем лямбда функцию для кортежей число и его квадрат

# print(res)

# # where --> filter

# data = [x for x in range(1,20)]
# print(data)

# res = filter(lambda x: x%2 == 0, data) # результат работы функции filter, в которой опишем лямбду, проверяющую на чётность filter object - нужно преобразовать

# print(list(res))

## теперь применим filter вместо ранее описанной where

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 13 23 38'.split()

# res = map(int, data) # в качестве первого аргумента функция int, которая отвечает за преобразование строк в число

# res = filter(lambda x: not x%2, res ) # в качестве первого аргумента описываем лямбда функцию для чётных чисел

# res = list(map(lambda x: (x, x**2), res )) # в качестве первого аргумента описываем лямбда функцию для кортежей число и его квадрат

# print(res)

## zip

# # допустим есть набор данных

# users = ['user1', 'user2', 'user3', 'user4', 'user5'] # юзеры
# ids = [11, 23, 53, 34, 95] # идентификаторы
# salary = [5467,890,345]
# data = zip (users, ids) # получаем кортежи соответствующих индексов списков  - zip object 
# print(list(data))

# data = list(zip (users, ids, salary)) # zip пробекается по минимальному входящему набору (в данном случае по salary) 
# print(data)


## enumerate

users = ['user1', 'user2', 'user3', 'user4', 'user5'] # юзеры
data = list(enumerate (users)) # на выходе получаем кортежи номер юзера и юзер 
print(data)


