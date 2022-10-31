# Создайте программу для игры в "Крестики-нолики".

def DrawBoard (boardLocal):
    print(f' {boardLocal[0][0]} | {boardLocal[0][1]} | {boardLocal[0][2]}')
    print('-----------')
    print(f' {boardLocal[1][0]} | {boardLocal[1][1]} | {boardLocal[1][2]}')
    print('-----------')
    print(f' {boardLocal[2][0]} | {boardLocal[2][1]} | {boardLocal[2][2]}')



def GetWinningSymbol(boardLocal):
    
    for i in boardLocal:
        if i[0] == i[1] and i[1] == i[2] and i[0] != ' ':
            return i[0]
    for i in range(3):
        if boardLocal[0][i] == boardLocal[1][i] and boardLocal[1][i] == boardLocal[2][i] and boardLocal[0][i] != ' ':
            return boardLocal[0][i]
    if boardLocal[0][0] == boardLocal[1][1] and boardLocal[1][1] == boardLocal[2][2] and boardLocal[0][i] != ' ':
        return boardLocal[0][0]
    if boardLocal[2][0] == boardLocal[1][1] and boardLocal[1][1] == boardLocal[0][2] and boardLocal[0][i] != ' ':
        return boardLocal[2][0]
    
    return ''

def FullCheck(boardLocal):
    
    for i in boardLocal:
        for j in i:
            if j == ' ':
                return False
    return True


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
SymbolToMove = 'X'
DrawBoard(board)

while len(GetWinningSymbol(board)) == 0 and not FullCheck(board):
    row = int(input(f'ход {SymbolToMove}-иков! Введите строку хода: '))
    column = int(input(f'ход {SymbolToMove}-иков! Введите столбец хода: '))
    while board[row - 1][column - 1] != ' ':
        print('Выберете пустое поле!')
        row = int(input(f'ход {SymbolToMove}-иков! Введите строку хода: '))
        column = int(input(f'ход {SymbolToMove}-иков! Введите столбец хода: '))

    board[row - 1][column - 1] = SymbolToMove

    if SymbolToMove == 'X':
        SymbolToMove = 'O'
    else:
        SymbolToMove = 'X'
    DrawBoard(board)
    
if not FullCheck(board):
    print(f'Победа {GetWinningSymbol(board)}-иков!')
else:
    print('Ничья!')