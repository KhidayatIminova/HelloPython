# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.



# en_text = input("Введите текст для кодировки: ")

path1 = 'tsk5-61.txt'
path2 = 'tsk5-62.txt'

f = open(path1, 'r')
en_text = f.read()
f.close

import os         
os.system('cls')

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 

    if not data:
        return '' 

    for char in data: 
        if char != prev_char: # если текущий символ не совпадает с предыдущим
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char 
        else:  # если символы совпадают, увеличиваем счетчик на 1
            count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): # Если символ является цифрой
            count += char # кладем его в переменную count (если стоят 2 цифры подряд, то соответственно в count будет 2 символа и т.д.  )  
        else: 
            decode += char * int(count) # иначе преобразуем count в число и соответственно дублируем символ count раз
            count = '' # очищаем count
    return decode

enc=rle_encode(en_text)
print(f"Текст после кодировки: {rle_encode(en_text)}")

dec_text=rle_decode(enc)
print(f"Текст после дешифровки: {dec_text}")

f = open(path2, 'w')
f.write(dec_text)
f.close