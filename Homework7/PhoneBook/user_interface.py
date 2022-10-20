def get_data ():
    data = []
    last_name = input('Введите фамилию: ')
    data.append(last_name)
    first_name = input('Введите имя: ')
    data.append(first_name)
    second_name = input('Введите отчество: ')
    data.append(second_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите 11-значный номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except ValueError:
            print('Неправильно набран номер.')
    data.append(phone_number)
    city = input('Введите место жительства: ')
    data.append(city)
    description = input('Введите описание: ')
    data.append(description)
    return data
