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

