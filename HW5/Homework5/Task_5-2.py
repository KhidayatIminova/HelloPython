# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"

import os         
os.system('cls')

from random import randint

candies = 56
lot = randint(1,2)

player1='Анечка'
player2='Вовочка'

if lot == 1:
    print (f'Результат жеребьёвки: 1-й ход делает {player1}. Брать не больше 28-ми конфет за раз!!!')
else:
    print (f'Результат жеребьёвки: 1-й ход делает {player2}. Брать не больше 28-ми кофет за раз!!!')

def InputNumber (player):   
    check_input = False
    input_number = 0
    while not check_input:
        try:
            input_number = int(input(f'{player}, возьми конфетку - сколько ты хочешь?: '))
            if input_number < 1 or input_number > 28:
                print(f"{player}, а морда не треснет от такого количества? ;) Попробуй ещё ) ")
                check_input = False
            else:
                check_input = True
        except ValueError:
            print ('Может еще раз? ')     
    return input_number

def p_print(name, k, value):
    print(f"{name} взял {k}, на столе осталось  {value} конфет.")

def game(player1, player2, lot, candies):
    while candies > 28:
        if lot == 1:
            k = InputNumber(player1)
            candies -= k
            lot = 2
            p_print(player1, k, candies)
        else:
            k = InputNumber(player2)
            # counter2 += k
            candies -= k
            lot = 1
            p_print(player2, k, candies)
    return lot

game(player1,player2,lot,candies)

if lot == 1:
    print(f'Победил {player1}!!!')
else:
    print(f'Победил {player2}!!!')
