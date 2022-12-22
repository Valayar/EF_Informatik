from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back
BUCHSTABENLISTE = ['A','B','C','D','E']
board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]
def Feld_abrufen():
    Zeilenzähler = 0
    print( ' ',  end='' )
    for i in range(len(board[0])):
        print( '', i+1, end='' )           
    print(' ')     



    for zeile in board:
        
        print(' ', end='')
        for zelle in zeile:
            print(Fore.GREEN + ' -', end='')
        print(' ')
        print( BUCHSTABENLISTE[Zeilenzähler], end='')
        for zelle in zeile:
            print(Fore.GREEN +f'|', end='')
            print(Back.RED +f'{zelle}', end='')
        print(Fore.GREEN + '|')
        Zeilenzähler = Zeilenzähler + 1
    print( ' ',  end='' )
    for zelle in board[0]:
        print(Fore.GREEN + ' -', end='')
    print(' ')


def input_check():
        input_viable = False 
        while input_viable == False:
            Input = input('Geben sie das gewünschte feld ein (Format: A1 , a1)')
            Input = list(Input)
            print(len(Input))
            if len(Input) > 2:
                print('Die Eingabe ist zu lang, versuchen sie es nochmals')
                input_check()
            if len(Input) < 2:
                print('Die Eingabe ist zu kurz, versuchen sie es nochmals')
                input_check()
            if Input[0] in 'abcde':
                BUCHSTABEN = ['A', 'B', 'C', 'D', 'E']
                Input[0] = 'abcde'.index(Input[0])
                Input[0] = BUCHSTABEN[Input[0]]
            if Input[0] in 'ABCDE':
                if Input[1] in '12345':
                    print('korrekte Eingabe')
                    global Input_Checked
                    Input_Checked = Input
                    input_viable = True
                
                else:
                    print('Zweite Ziffer ≠ 1, 2, 3, 4, 5  ')
            else:
                print('Erste Ziffer ≠ A,a,B,b,C,c,D,d,E,e  ')
       



Input_Checked = []
def Eingabe():
    input_check()
    print(Input_Checked)
    Input_Checked[0] = 'ABCDE'.index(Input_Checked[0])
    Input_Checked[1] = int(Input_Checked[1])
    Input_Checked[1] = Input_Checked[1] - 1


    oldfieldvalue = board[Input_Checked[0]][Input_Checked[1]]
         
    def flood_fill(x ,y, old, new): 
        print(x,y,old,new)
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):         
            return
        if board[x][y] != old:
            return
        Feld_abrufen()
        board[x][y] = new
        flood_fill(x+1, y, old, new)
        flood_fill(x-1, y, old, new)
        flood_fill(x, y+1, old, new)
        flood_fill(x, y-1, old, new)

    flood_fill(Input_Checked[0],Input_Checked[1],board[Input_Checked[0]][Input_Checked[1]], ' ')
    
    board[Input_Checked[0]][Input_Checked[1]] = oldfieldvalue * 2


'''
def field_rearrange():
    for line in board:
        print (line)
        for collum in line:
            print (collum)
            if collum == ' ':
                print([collum])
                board[1][1] = 1

    print(board)
'''   

    









        


    




customfunc = True
while customfunc == True :
    Feld_abrufen()
    Eingabe()
    Feld_abrufen()
    '''field_rearrange()'''
    
    






    # Quellenangaben: 
    # https://de.wikipedia.org/wiki/Floodfill
    # https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569    
