#Schreiben Sie eine Funktion pprint (Abkürzung für Pretty Print), welche eine 2D-Liste übersichtlich ausgibt:

#pprint([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Ausgabe bspw.
# [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
# ]

def pprint(mat2d):
    for zeile in mat2d:
        print(zeile)

pprint([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
