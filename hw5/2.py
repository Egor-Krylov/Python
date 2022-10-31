# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random

def GetBotNextMove(candiesLeft):
    if (candiesLeft % 29 > 0):
        return candiesLeft % 29
    else:
        return random.randint(1, 28)

regime = -1
moveCount = 0
moveCandies = 0
candies = int(input('Введите количество конфет: '))
players = [input('Введите имя первого игрока: ')]
while regime != 0 and regime != 1:  
    regime = int(input('Введите 0, чтобы играть вдвоем или 1, чтобы играть против бота: '))
    if regime != 0 and regime != 1:  
        print('Введите 0 или 1')


if regime == 0:
    firstMovePlayer = random.randint(0, 1)
    players.append(input('Введите имя второго игрока: '))
else:
    if (candies % 29 > 0):
        firstMovePlayer = 1
    else:
        firstMovePlayer = 0
    players.append('бот "Сладкоежка-M"')

print(f'Первым ходит {players[firstMovePlayer]}')

while candies > 0:
    playerToMove = (moveCount + firstMovePlayer) % 2
    while not (0 < moveCandies < 29):
        if (regime == 0) or (regime == 1 and playerToMove == 0):
            moveCandies = int(input(f'{players[playerToMove]}, сколько конфет вы заберете? (1 - 28): '))
        else:
            moveCandies = GetBotNextMove(candies)
            print(f'бот "Сладкоежка-M" забирает {moveCandies} конфет')
            
    if (candies - moveCandies) > 0:
        candies -= moveCandies 
        print(f'Осталось конфет: {candies}')
    else:
        print(f'Осталось 0 конфет, {players[playerToMove]} победил!')
        candies = 0
    moveCount += 1
    moveCandies = 0



