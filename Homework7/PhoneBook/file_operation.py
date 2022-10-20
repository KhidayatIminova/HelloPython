from user_interface import get_data as gd

info = gd()
def writing_csv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
       data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nОтчество: {info[2]}\nНомер телефона: {info[3]}\nГород: {info[4]}\nОписание: {info[5]}\n\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nОтчество: {info[2]}\nНомер телефона: {info[3]}\nГород: {info[4]}\nОписание: {info[5]}\n\n')

def open_csv ():
    with open('Phonebook.csv', 'r', encoding = 'utf-8') as data:
        text_phone = data.read()
    print(text_phone)