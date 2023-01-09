# Arbeit an NumTrip

 # Nachbarzellen Kombinieren

 **Floodfill**

Das Prinzip einer Floodfill funktion ist ja noch relativ einfach zu verstehen. Wie diese in der Programmierspache implementiert wird, ist eine andere Sache. zunächst hatte ich mir den zugehörenden Wikipediaeintrag dazu angeschaut. 

jedoch konnte ich mir den unterschied von diesen zwei Codeblöcken nicht erklären.


```py
def fill4(x, y, alteFarbe, neueFarbe):
    if getPixel(x, y) == alteFarbe:
        setPixel(x, y, neueFarbe)
        fill4(x, y + 1, alteFarbe, neueFarbe)  # unten
        fill4(x, y - 1, alteFarbe, neueFarbe)  # oben
        fill4(x + 1, y, alteFarbe, neueFarbe)  # rechts
        fill4(x - 1, y, alteFarbe, neueFarbe)  # links
```

```py
def fill4(x, y, alteFarbe, neueFarbe):
    stack.push(x, y)
    while stack.isNotEmpty():
        (x, y) = stack.pop()
        if getPixel(x, y) == alteFarbe:
            setPixel(x, y, neueFarbe)
            stack.push(x, y + 1)
            stack.push(x, y - 1)
            stack.push(x + 1, y)
            stack.push(x - 1, y)
```

Der obere ist ganz allgemein, der andere ist primär für Phyton. 

Ich habe mir noch ein noch ein Praxisbeispiel zum Floodfill-Algorythmus angeschaut. 
Durch dieses habe ich die Anwendung besser verstehen können. 

```py
def flood_fill(x ,y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return
    # secondly, check if the current position equals the old value
    if field[y][x] != old:
        return
    
    # thirdly, set the current position to the new value
    field[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)
```
Dieses Beispiel löst das Problem des oberen Algorythmus welcher nicht erkennt kann ob man sich innerhalb des Feldes befindet. Weil sobald ein Feld ausserhalb der Liste verändert werden soll, bekommen wir die Fehlermeldung: **IndexError: list index out of range** 

Ich habe diesen Beispielscode modifiziert und in meinem NumTrip Game implementiert. 

Quellenangaben:  
[Wikipediaeintrag Floodfill](https://de.wikipedia.org/wiki/Floodfill)  
[A Python Example of the Flood Fill Algorithm
](https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569)

# Felder Auffüllen


Dieser Teil des Spieles ist eigentlich Ziemlich simpel. wir müssen eine Funktion programmieren, welche bei leeren Feldern die Zahl aus dem Feld darüber nimmt. 

Später müssen wir der Funktion noch die Möglichkeit geben bei den Obersten Feldern eine zufällige Zahl zu importieren. 

Da mir dieses Problem zu gross war, habe ich zuerst in einem Seperaten Dokument gearbeitet. 

* Vorgehensweise:
* 1. Simple Liste erstellen 
* 2. Für jeden einzelnen Wert in den Zeilen wiederholen 
* 3. Falls oberste Zeile, zufallszahl einfügen 
* 4. mithilfe des Indexes werte von Feldern überschreiben
* 5. Für jede Zeile wiederholen 

Ich habe noch keine bessere Option dafür gefunden als das Programm für jede Zele zu wiederholen, da ich keine gute möglichkeit hatte zu überprüfen ob es keine Leeren felder auf dem Spielfeld gibt. 

````py
field = [[1,2, ' '], [' ',' ', ' '],[ ' ', ' ' , ' ']]  # 1.
save = []

import random
random.seed(2)
numbers = [1, 2, 4, 8]

def fieldrearrange():
    for i in range(5):     # 5. 
        for x in field:

            print(field.index(x))
            for y in x :                # 2. 
                
                print(x.index(y))
                if y == ' ' :

                    if field.index(x) <= 0:                            # 3. 
                        field[0][x.index(y)] = random.choice(numbers)
            
                    if field.index(x) > 0:      # 4. 
                        save = field[field.index(x) - 1][x.index(y)]
                        field[field.index(x) - 1][x.index(y)] = ' '
                        field[field.index(x)][x.index(y)] = save
                        save = []

fieldrearrange()   
print(field)
````



