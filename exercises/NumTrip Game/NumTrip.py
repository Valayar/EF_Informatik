from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back

import random
random.seed(2)
MAX_POTENZ_START = 3
from random import *
numbers = [1, 2, 4, 8]
Letter_List = ['A', 'B', 'C', 'D', 'E']
letter_list = ['a', 'b', 'c', 'd', 'e']
Input_Checked = []
count = 0
move_ok = True
board = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]for i in range(5)]
printed = [[], [], [], [], []]


def print_field():  # printet die 2D Liste 'board'
    print('    1    2    3    4    5  \n  +----+----+----+----+----+')
    for i in range(5):
        for j in range(5):
            for k in range(3):
                if int(board[i][j]) < 10**(k + 1):
                    printed[i].append(f'{board[i][j]}' + (2 - k) * ' ')
                    break
        print(f' {Letter_List[i]}| {printed[i][0]}| {printed[i][1]}| {printed[i][2]}| {printed[i][3]}| {printed[i][4]}|')
        print('  +----+----+----+----+----+ ')


def Input_check():  # fragt die person nach Input, prüft diesen auf korrektheit
    Input_viable = False
    while Input_viable == False:
        eingabe = input('-' * 50 + '\nGeben sie das gewünschte feld ein (Format: A1 , a1)\n ' + '-' * 50 + '\n')
        eingabe = eingabe.strip()
        eingabe = eingabe.lower()
        print(eingabe)
        Input = [[], []]
        Input[0].append(eingabe[0:1])
        Input[1].append(eingabe[1:2])
        if Input[0] in letter_list:
            Input[0] = 'abcde'.index(Input[0])

            if Input[1] in '12345':
                global Input_Checked
                Input_Checked = Input
                Input_viable = True
                return Input_Checked

            else:
                print('Zweite Ziffer ≠ 1, 2, 3, 4, 5  ')
        else:
            print('Erste Ziffer ≠ A,a,B,b,C,c,D,d,E,e  ')


def User_Input():  # sucht nach machbaren Zug, floodfill setzt Felder mit gleichem Wert auf ' ', verdoppelt ausgewählter Wert des Feldes
    global move_ok
    move_ok = False
    while not move_ok:  # prüft ob das Feld einen Nachbarn hat
        Input_Checked = Input_check()
        # bearbeitet die liste mit dem Input so damit sie in "board" verwendet werden kann
        Input_Checked[0] = 'abcde'.index(Input_Checked[0])
        Input_Checked[1] = int(Input_Checked[1])
        Input_Checked[1] = Input_Checked[1] - 1
        move_not_possible()

    oldfieldvalue = board[Input_Checked[0]][Input_Checked[1]]

    def flood_fill(x, y, old, new):
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return
        if board[x][y] != old:
            return
        board[x][y] = new
        flood_fill(x + 1, y, old, new)
        flood_fill(x - 1, y, old, new)
        flood_fill(x, y + 1, old, new)
        flood_fill(x, y - 1, old, new)

    flood_fill(Input_Checked[0], Input_Checked[1], board[Input_Checked[0]][Input_Checked[1]], ' ')

    board[Input_Checked[0]][Input_Checked[1]] = oldfieldvalue * 2       # Prüft ob 1024 erreicht wurde -> Spiel gewonnen
    if oldfieldvalue * 2 == 64:
        print_field()
        game_won('-' * 50 + '\nDu hast in ', count, 'Zügen gewonnen!\n' + '-' * 50)


def fieldrearrange():  # ersetzt Felder mit dem Wert ' ' mit dem Wert des obersten Feldes, oberstes Feld
    for i in range(7):
        for x in board:
            for y in x:
                if y == ' ':
                    if board.index(x) <= 0:
                        board[0][x.index(y)] = random.choice(numbers)

                    if board.index(x) > 0:
                        save = board[board.index(x) - 1][x.index(y)]
                        board[board.index(x) - 1][x.index(y)] = ' '
                        board[board.index(x)][x.index(y)] = save
                        save = []


def move_not_possible():  # überprüft ob ausgewähltes feld ein Nachbarfeld mit gleichem Wert hat
    x = Input_Checked[0]
    y = Input_Checked[1]
    global move_ok

    if (x + 1) <= 4:
        if board[x + 1][y] == board[x][y]:
            move_ok = True
            return
    if (x - 1) >= 0:
        if board[x - 1][y] == board[x][y]:
            move_ok = True
            return
    if (y + 1) <= 4:
        if board[x][y + 1] == board[x][y]:
            move_ok = True
            return
    if (y - 1) >= 0:
        if board[x][y - 1] == board[x][y]:
            move_ok = True
        else:
            print_field()
            print('-' * 50, '\nDieser Zug ist nicht Möglich')
            move_ok = False
    else:
        print_field()
        print('-' * 50, '\nDieser Zug ist nicht Möglich')
        move_ok = False


def reset():  # ersetzt alle Zahlen auf dem Feld mit einem leeren Wert
    global board
    board = [[(2**(randint(1, MAX_POTENZ_START + 1))) for i in range(5)]for i in range(5)]
    global count
    count = 0


def game_won(frage):  # gibt aus ob das Spiel gewonnen wurde + replay
    print(frage)
    input_check_replay = 'False'
    replay = input('Möchtest du nochmal Spielen? (Ja / Nein)\n' + '-' * 50 + '\n')
    while input_check_replay != 'True':
        if replay.strip() in ['ja', 'Ja']:
            input_check_replay = 'True'
            reset()
            return
        if replay.strip() in ['nein', 'Nein']:
            input_check_replay = 'True'
            global game_start
            game_start = 'True'
        else:
            replay = input('-' * 50 + '\nMöchtest du nochmal Spielen? (Ja / Nein)' + '-' * 50 + '\n')


def loose():  # prüft ob das Spiel verloren wurde, und gibt einsprechenden output + replay
    global game_start
    no_neighbour_count = 0
    for y in range(5):
        for x in range(5):
            z = 0
            if x != 4:
                if board[x + 1][y] != board[x][y]:
                    z = z + 1
            else:
                z = z + 1
            if x != 0:
                if board[x - 1][y] != board[x][y]:
                    z = z + 1
            else:
                z = z + 1
            if y != 4:
                if board[x][y + 1] != board[x][y]:
                    z = z + 1
            else:
                z = z + 1
            if y != 0:
                if board[x][y - 1] != board[x][y]:
                    z = z + 1
            else:
                z = z + 1
            if z == 4:
                no_neighbour_count = no_neighbour_count + 1
    if no_neighbour_count == 25:
        print('Sie haben in', count, 'Zügen veloren!')
        input_check_replay = 'False'
        replay = input(
            '---------------------------------------------------\nMöchtest du nochmal Spielen? (Ja / Nein)\n---------------------------------------------------')
        while input_check_replay != 'True':
            if replay.strip() in ['ja', 'Ja']:
                input_check_replay = 'True'
                reset()
                return
            if replay.strip() in ['nein', 'Nein']:
                input_check_replay = 'True'
                global game_start
                game_start = False

            else:
                replay = input(
                    '---------------------------------------------------\nMöchtest du nochmal Spielen? (Ja / Nein)\n---------------------------------------------------')


def counter():  # zählt die gemachten Züge
    global count
    count = count + 1
    print('-' * 50 + '\nZug ', count)


game_start = True
while game_start == True:
    loose()
    print_field()
    counter()
    User_Input()
    fieldrearrange()
