def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return input()

def input_data():
    print('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (используйте формат: "a+bj"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "a+bj"):')
        right_value = get_value()
        print('Выберите операцию: (+, -. * или /)')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "a/b"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "a/b"):')
        right_value = get_value()
        print('Выберите операцию: (+, -. * или /)')
        oper = get_value()
    return (data_type, left_value, oper, right_value)