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

def Eingabe():
    eingabe = input('Geben sie das gewünschte feld ein (Format: A1)')
    eingabe = list(eingabe)
    eingabe[0] = 'ABCDE'.index(eingabe[0])
    eingabe[1] = int(eingabe[1])
    eingabe[1] = eingabe[1] - 1
    print(eingabe)
         
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

    flood_fill(eingabe[0],eingabe[1],board[eingabe[0]][eingabe[1]], ' ')

customfunc = True
while customfunc == True :
    Feld_abrufen()
    Eingabe()
    






    # Quellenangaben: 
    # https://de.wikipedia.org/wiki/Floodfill
    # https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569    
