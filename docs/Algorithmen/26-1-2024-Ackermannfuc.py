#Ackermann funktion, ist eine sehr schwierig zu computierende Funktion
#berechnet aus zwei Eingangswerten einen Ausganswert
#VSC bricht bei gewissen Werten ab, da die zu lange zu computieren müssten

import random

def ack(m,n):
    if m == 0:
        anw = n+1

    else:
        if n == 0:
            anw = ack(m-1, 1)
        else:
            anw = ack(m-1,ack(m,n-1))
    return anw

#nimm 5x 2 zufallszahlen von 1-4 
#nicht immer ausgabe möglich
for i in range(5):
    m = random.randint(1,4)
    n = random.randint(1,4)
    print(m, n, ack(m,n))
        
    