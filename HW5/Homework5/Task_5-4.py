# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"

import os         
os.system('cls')

# человек против бота с "интеллектом"

from random import randint

sweet_candies = 102

player1='Анечка'
player2='Бот'

turn = randint(0,1) # идентификатор очереди хода
if turn == 0:
    print (f'На столе лежит {sweet_candies} конфет. \nРезультат жеребьёвки: 1-й ход делает {player1}. Брать не больше 28-ми конфет за раз!!!')
else:
    print (f'На столе лежит {sweet_candies} конфет. Результат жеребьёвки: 1-й ход делает {player2}. Брать не больше 28-ми конфет за раз!!!')

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

def get_winner(sweet, turn_win):
    if turn_win == 0:
        print(f'И сделав последний ход, забрав со стола оставшиеся {sweet} конфет побеждает {player1}!!!\n')
    else:
        print(f'И сделав последний ход, забрав со стола оставшиеся {sweet} конфет побеждает {player2}!!!\n')

def ai(sweet):

    if 30 < sweet < 57: # когда остаток конфет меньше или равен (28 + 28) бот может проиграть Анечке, забрав слишком много конфет

        # k = sweet - 29 # поэтому так он может выиграть бедняжку Анечку 

        k = randint(1,sweet-30) # или дать ей шанс ): поэтому он будет выбирать такие числа, чтобы результат не вышел за пределы неснижаемого остатка +1, т.е был >= 29
        
    elif sweet == 30:
        k = 1 # шанс шансом, но поддаваться Анечке Бот не станет
    else:
        k = randint(1, 28) # а в остальных случаях как рандом решит
    return k

def game(player1, player2, turn, sweet):
    while sweet > 28: # исходя из условия задачи, последний ход =<28, 
        if turn == 0:
            k = InputNumber(player1)
            sweet -= k
            turn = 1
            print(f'На столе осталось {sweet} конфет\n')
        else:
            k = ai(sweet)
            # if 30 < sweet < 57:
            #     k = randint(1,sweet-30)
            # elif sweet == 30:
            #     k = 1
            # else:
            #     k = randint(1, 28)
            sweet -= k
            turn = 0
            print(f'Бот взял {k} конфет')
            print(f'На столе осталось {sweet} конфет\n')
    get_winner(sweet, turn)
    return sweet, turn

game(player1,player2,turn,sweet_candies)








