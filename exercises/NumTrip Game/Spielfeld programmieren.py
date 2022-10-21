from colorama import init
init()
init(autoreset=True)
from colorama import Fore, Back

board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

for zeile in board:
    for zelle in zeile:
        print(Fore.GREEN + ' -', end='')
    print(' ')
    for zelle in zeile:
        print(Fore.GREEN +f'|', end='')
        print(Back.RED +f'{zelle}', end='')
    print(Fore.GREEN + '|')

for zelle in board[0]:
    print(Fore.GREEN + ' -', end='')
print(' ')











