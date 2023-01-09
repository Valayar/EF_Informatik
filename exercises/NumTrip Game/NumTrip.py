from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back
Letter_List = ['A','B','C','D','E']
board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]
def Feld_abrufen():
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
            Input = input('Geben sie das gewünschte feld ein (Format: A1 , a1)')
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
                    print('korrekte Eingabe')
                    global Input_Checked
                    Input_Checked = Input
                    Input_viable = True
                
                else:
                    print('Zweite Ziffer ≠ 1, 2, 3, 4, 5  ')
            else:
                print('Erste Ziffer ≠ A,a,B,b,C,c,D,d,E,e  ')
       



Input_Checked = []
def User_Input():
    Input_check()
    
    Input_Checked[0] = 'ABCDE'.index(Input_Checked[0])
    Input_Checked[1] = int(Input_Checked[1])
    Input_Checked[1] = Input_Checked[1] - 1


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
    
    board[Input_Checked[0]][Input_Checked[1]] = oldfieldvalue * 2



import random
random.seed(2)
numbers = [1, 2, 4, 8]
print(random.choice(numbers))


def fieldrearrange():
    for i in range(5):
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
                    

        

customfunc = True
while customfunc == True :
    Feld_abrufen()
    User_Input()
    fieldrearrange()
    
    
    






    # Quellenangaben: 
    # https://de.wikipedia.org/wiki/Floodfill
    # https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569    
