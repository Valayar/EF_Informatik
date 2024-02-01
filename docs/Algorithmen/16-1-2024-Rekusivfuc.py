#rekusive Funktion, welche jeweils die fakultät einer Zahl berechnet (n!)

def faktor(n):
    if n == 1:
        return n
    else:
        return n * faktor(n-1)

#ruft die rekursive Funktion für die Werte 1-10 auf
for i in range(10):
    print(i+1, faktor(i+1))

