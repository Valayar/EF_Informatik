from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back

import random
random.seed(2)

numbers = [1, 2, 4, 8]
Letter_List = ['A','B','C','D','E']
Input_Checked = []
count = 0
move_ok = True
board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

def print_field():
    line_counter = 0
    print( ' ',  end='' )
    for i in range(len(board[0])):
        print( '', i+1, end='' )           
    print(' ')     
    for line in board:
        
        print(' ', end='')
        for cell in line:
            print(Fore.GREEN + ' -', end='')
        print(' ')
        print( Letter_List[line_counter], end='')
        for cell in line:
            print(Fore.GREEN +f'|', end='')
            print(Back.RED +f'{cell}', end='')
        print(Fore.GREEN + '|')
        line_counter = line_counter + 1
    print( ' ',  end='' )
    for cell in board[0]:
        print(Fore.GREEN + ' -', end='')
    print(' ')

def Input_check():
        Input_viable = False 
        while Input_viable == False:
            Input = input('-'*50 +'\nGeben sie das gewünschte feld ein (Format: A1 , a1)\n '+'-'*50 + '\n')
            Input = list(Input)
            
            if len(Input) > 2:
                print('Die Eingabe ist zu lang, versuchen sie es nochmals')
                continue
            if len(Input) < 2:
                print('Die Eingabe ist zu kurz, versuchen sie es nochmals')
                continue
            if Input[0] in 'abcde':
                Input[0] = 'abcde'.index(Input[0])
                Input[0] = Letter_List[Input[0]]
            if Input[0] in 'ABCDE':
                if Input[1] in '12345':
                    global Input_Checked
                    Input_Checked = Input
                    Input_viable = True
                
                else:
                    print('Zweite Ziffer ≠ 1, 2, 3, 4, 5  ')
            else:
                print('Erste Ziffer ≠ A,a,B,b,C,c,D,d,E,e  ')
    
def User_Input():
    global move_ok
    move_ok = False
    while move_ok == False:                                             #prüft ob das Feld einen Nachbarn hat 
        Input_check()
        Input_Checked[0] = 'ABCDE'.index(Input_Checked[0])              #bearbeitet die liste mit dem Input so damit sie in "board" verwendet werden kann
        Input_Checked[1] = int(Input_Checked[1])
        Input_Checked[1] = Input_Checked[1] - 1
        move_not_possible()
            

    oldfieldvalue = board[Input_Checked[0]][Input_Checked[1]]
         
    def flood_fill(x ,y, old, new): 
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):         
            return
        if board[x][y] != old:
            return
        board[x][y] = new
        flood_fill(x+1, y, old, new)
        flood_fill(x-1, y, old, new)
        flood_fill(x, y+1, old, new)
        flood_fill(x, y-1, old, new)

    flood_fill(Input_Checked[0],Input_Checked[1],board[Input_Checked[0]][Input_Checked[1]], ' ')
    
    
    board[Input_Checked[0]][Input_Checked[1]] = oldfieldvalue * 2       # Prüft ob 1024 erreicht wurde -> Spiel gewonnen
    if oldfieldvalue * 2 == 64:
        print_field()
        game_won() 

def fieldrearrange():
    for i in range(7):
        for x in board:
            for y in x :
                if y == ' ' :
                    if board.index(x) <= 0:
                        board[0][x.index(y)] = random.choice(numbers)
            
                    if board.index(x) > 0:
                        save = board[board.index(x) - 1][x.index(y)]
                        board[board.index(x) - 1][x.index(y)] = ' '
                        board[board.index(x)][x.index(y)] = save
                        save = []
                
def move_not_possible():
    x = Input_Checked[0]
    y = Input_Checked[1]
    global move_ok
    
    if (x + 1) <= 4: 
        if board[x+1][y] == board[x][y]:
            move_ok = True
            return       
    if (x - 1) >= 0:
        if board[x-1][y] == board[x][y]:
            move_ok = True
            return
    if (y + 1) <= 4:
        if board[x][y+1] == board[x][y]:
            move_ok = True
            return
    if (y - 1) >= 0:
        if board[x][y-1] == board[x][y]:
            move_ok = True
        else: 
            print_field()
            print('-'*50,'\nDieser Zug ist nicht Möglich')
            move_ok = False   
    else: 
        print_field()
        print('-'*50,'\nDieser Zug ist nicht Möglich')
        move_ok = False         

def reset():
    global board
    board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]
    global count
    count = 0

def game_won():
    print('-'*50 +'\nDu hast in ', count, 'Zügen gewonnen!\n' + '-'*50 )
    input_check_replay = 'False'
    replay = input('Möchtest du nochmal Spielen? (Ja / Nein)\n' + '-'*50 +'\n')
    while input_check_replay != 'True' :
        if replay.strip() in ['ja', 'Ja']:
            input_check_replay = 'True'
            reset()
            return
        if replay.strip() in ['nein', 'Nein']:
            input_check_replay = 'True'
            global game_start
            game_start = 'True' 
        else:    
            replay = input('-'*50 +'\nMöchtest du nochmal Spielen? (Ja / Nein)' + '-'*50 +'\n')

def loose():
    global game_start
    a=0
    for y in range(5):
        for x in range(5):
            z=0
            if x!=4:
                if board[x+1][y]!=board[x][y]:
                    z=z+1
            else:
                z=z+1
            if x!=0:
                if board[x-1][y]!=board[x][y]:
                    z=z+1
            else:
                z=z+1
            if y!=4:
                if board[x][y+1]!=board[x][y]:
                    z=z+1
            else:
                z=z+1
            if y!=0:
                if board[x][y-1]!=board[x][y]:
                    z=z+1
            else:
                z=z+1
            if z==4:
                a=a+1
    if a==25:
        print ('Sie haben in', count ,'Zügen veloren!')
        input_check_replay = 'False'
        replay = input('---------------------------------------------------\nMöchtest du nochmal Spielen? (Ja / Nein)\n---------------------------------------------------')
        while input_check_replay != 'True' :
            if replay.strip() in ['ja', 'Ja']:
                input_check_replay = 'True'
                reset()
                return
            if replay.strip() in ['nein', 'Nein']:
                input_check_replay = 'True'
                global game_start
                game_start = False
                
            else:    
                replay = input('---------------------------------------------------\nMöchtest du nochmal Spielen? (Ja / Nein)\n---------------------------------------------------')
            
def counter():
    global count
    count = count + 1
    print('-'*50 + '\nZug ' , count)

game_start  = True
while game_start == True :
    loose()
    print_field()
    counter()
    User_Input()
    fieldrearrange()
    