# Arbeit an NumTrip

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

Quellenangaben:  
[Wikipediaeintrag Floodfill](https://de.wikipedia.org/wiki/Floodfill)  
[A Python Example of the Flood Fill Algorithm
](https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569)