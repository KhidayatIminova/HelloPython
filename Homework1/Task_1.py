# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = (input('Введите число дня недели от 1 до 7: '))

print(type(a))
print(a.isdigit())

def Week_days (num):
    
    if int (num) == 6 or int (num) ==7:
        print("Выходной")
    elif 0 < int (num) < 6:
        print("Рабочий день")
    
if a.isdigit() == True and 0 < int (a) < 8:
    Week_days (a)
else:
     print('Правильна цыфры тыкай!!')

