# Variablen

from ctypes.wintypes import SIZE
from operator import ge
import zufallsworte as zufall

wort = zufall.zufallswoerter(1)[0].lower()  # gibt ein Zufallswort zurück


gesucht = wort


gefunden = []
falsch_geraten = []


def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')


def is_valid(inp):
    return True


def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()


def auswerten(valid_inp):
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)


def gewonnen():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True
        







def game_over():
            size = 1
            for x in falsch_geraten:
                size+=1
            print(size, len(falsch_geraten))
            Versuche = 3
            if size == Versuche:
                print('ALARM GAME OVER')
                return True
            else:
        
                return False

def play():
    while not game_over():
        BUCHSTABE = eingabe() 
        auswerten(BUCHSTABE)
        show()
        print(gefunden)
        print(gesucht)
       
    if gewonnen():
        print('Du hast das Wort erraten!')
    else:
        print('Du hast verloren!')


print(wort)

play()





