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


eingabe = input('Geben sie das gewünschte feld ein (Format: A1)')

print (eingabe)
eingabe = list(eingabe)
print (eingabe)

'''
BUCHSTABENLISTE = ['A','B','C','D','E']

for BUCHSTABENLISTE in eingabe:
    eingabe[0] = 1
'''

if eingabe[0] == 'A' :
    eingabe[0] = int(0)
elif eingabe[0] == 'B' :
    eingabe[0] = int(1)
elif eingabe[0] == 'C' :
    eingabe[0] = int(2)
elif eingabe[0] == 'D' :
    eingabe[0] = int(3)
elif eingabe[0] == 'E' :
    eingabe[0] = int(4)
else:
    print ('Fehlerhafte Eingae!')

eingabe[1] = int(eingabe[1])
eingabe[1] = eingabe[1] - 1

print (eingabe) 

board[eingabe[0]][eingabe[1]]= ' '

Feld_abrufen()

'''
Feld_abrufen()

board[0][1] = ' '

Feld_abrufen()

board.insert ([4], [1])
Feld_abrufen()

board[1] [1] = 0
Feld_abrufen()

'''



