# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"

## Добавляем бота

import os         
os.system('cls')

from random import randint

candies = 56

player1='Анечка'
player2='Бот'

lot = randint(1,2)
if lot == 1:
    print (f'На столе лежит {candies} конфет. \nРезультат жеребьёвки: 1-й ход делает {player1}. Брать не больше 28-ми конфет за раз!!!')
else:
    print (f'На столе лежит {candies} конфет. Результат жеребьёвки: 1-й ход делает {player2}. Брать не больше 28-ми кофет за раз!!!')

def InputNumber (player):   
    check_input = False
    input_number = 0
    while not check_input:
        try:
            input_number = int(input(f'{player}, возьми конфетку - сколько ты хочешь?: '))
            if input_number < 1 or input_number > 28:
                print(f"{player}, а личико не треснет от такого количества? ;) Попробуй ещё ) ")
                check_input = False
            else:
                check_input = True
        except ValueError:
            print ('Может еще раз? ')     
    return input_number

def game(player1, player2, lot, candies):
    while candies > 0:
        if lot == 1:
            k = InputNumber(player1)
            candies -= k
            lot = 2
            print(f'На столе осталось {candies} конфет\n')
        else:
            # k = InputNumber(player2)
            k = randint(1,28) # вместо ввода с клавиатуры для второго игрока используем генератор случайных чисел
            candies -= k
            lot = 1
            print(f'\nБот взял {k} конфет. ')
            print(f'На столе осталось {candies} конфет\n')
    return lot

game(player1,player2,lot,candies)

if lot == 1:
    print(f'\nКонфеты на столе закончились! Победил(а) {player1}!!!')
else:
    print(f'\nКонфеты на столе закончились! Победил(а) {player2}!!!')
