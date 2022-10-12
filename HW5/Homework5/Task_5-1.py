# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os         
os.system('cls')

# txt = input_text = input(f'Введите текст: ')

txt = 'Шла Саша по шоссе и сосала сушку'

print(txt)
# print(type(txt))

txt1 = txt.split() # преобразуем строку в список с разделением по пробелам
# print(txt1)
# print(type(txt1))

del_txt = input_text = input(f'Какое недопустимое буквосочетание хотим найти и вымарать это грязное слово из текста?: ')

# print(txt.replace(del_txt, ''))
# print(len(txt1))

for i in range(len(txt1)):
    # print(txt1[i])
    # print(txt1[i].find(del_txt))
    if txt1[i].find(del_txt) != -1:
        txt1[i] = '!!!ВОЗМУТИТЕЛЬНО!!!'
        # txt1[i] = ''
       
    # print(type(txt1[i]))


# print(txt1)

txt1 = ' '.join(txt1)

print(txt1)
txt1 = txt1.replace('!!!ВОЗМУТИТЕЛЬНО!!!', '')
txt1 = txt1.replace('  ', ' ')
# print(type(txt1))
print(txt1)


