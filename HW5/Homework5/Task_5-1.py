# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os         
os.system('cls')

# txt = input_text = input(f'Введите текст: ')

txt = 'Шла Саша по шоссе, и сосала абвушку'

print(txt)
print()

del_txt = input_text = input(f'Какое буквосочетание хотим найти и удалить все слово из текста?: ')

def censored(txt1, del_txt):
    txt1 = txt.split() # преобразуем строку в список с разделением по пробелам
    count = 0
    for i in range(len(txt1)):

        if txt1[i].find(del_txt) != -1:
            txt1[i] = '!!!CENSORED!!!'
            count +=1
    txt1 = ' '.join(txt1)

    print(txt1)

    print(f'\nНайдено и удалено {count} слов, содержащих "{del_txt}"\n')
    txt1 = txt1.replace('!!!CENSORED!!! ', '')
    txt1 = txt1.replace('!!!CENSORED!!!', '')
    txt1 = txt1.replace('  ', ' ') # заменим двойные пробелы на одинарные

    print(txt1)

censored(txt, del_txt)

