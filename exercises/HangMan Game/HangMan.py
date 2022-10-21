# Variablen
gesucht = 'test'

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
    return False

def game_over():
    pass


def play():
    while not game_over():
        BUCHSTABE = eingabe() 
        auswerten(BUCHSTABE)
        show()
    if gewonnen():
        print('')
    else:
        print('')


play()

