
'''
Erzeugen Sie eine Liste mit den

+ ersten zehn Quadratzahlen
+ ersten zehn Zweierpotenzen
+ die Zweierpotenzen von 2 hoch 100 bis 2 hoch 110 
+ die natürlichen Zahlen rückwärts von 20 bis und mit 10
'''




squares = [ (i+1)**2 for i in range(10)]
power2 = [ i*2**2 for i in range(10)]
power2_100 = [ 2**i+100 for i in range(10)]

print(squares)
print(power2)
print(power2_100)