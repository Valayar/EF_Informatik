from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back

Zeilenzähler = 0
board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

print( ' ',  end='' )
for i in range(len(board[0])):
    print( '', i, end='' )           
print(' ')     


for zeile in board:
    Zeilenzähler = Zeilenzähler + 1
    print(' ', end='')
    for zelle in zeile:
        print(Fore.GREEN + ' -', end='')
    print(' ')
    print( Zeilenzähler, end='')
    for zelle in zeile:
        print(Fore.GREEN +f'|', end='')
        print(Back.RED +f'{zelle}', end='')
    print(Fore.GREEN + '|')

print( ' ',  end='' )
for zelle in board[0]:
    print(Fore.GREEN + ' -', end='')
print(' ')











