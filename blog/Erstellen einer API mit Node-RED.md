# Erfahrungen zum Erstellen einer API mit Node-RED 

## Postman
Postman ist ein Programm, welches dafür genutzt wird um HTTP Anfragen zu überprüfen. Diese Technik wird benötigt, falls man daran ist eine Webseite zu Programmieren und wissen muss was der Webserver als Antwort zurückgibt. So kann man testen ob alles Ordnungsgemäss funktioniert. Diese Technik wird auch benötigt falls man eine API programmiert/entwickelt. (Stichwort Bugfixing) Ich bin mir hierbei zwar nicht ganz sicher, aber ich glaube, dass man diese Technik benötigt, falls eine Webseite down ist und den genauen/ungefähren Fehler zu ermitteln. 

In unserem Beispiel haben wir mit Postman genutzt um auf unsere mit Node-RED erstellte API zuzugreifen.

**Warum Benötigt man Postman eigentlich?**
Man kann genauso die gewünschte Webadresse auch in einen Browser eingeben, und erhält dasselbe Resultat. 

*Der Grund dafür ist dieser: Wenn man es offline oder lokal ausprobieren möchte muss man Postman verwenden. Node-RED ist nach mir eine Ausnahme*

## Node-RED
Auf Node-RED besteht die von uns erstellte API aus verschiedenen "Workflows". In diesen Flows haben wir verschiedene Bausteine mit verschiedenen Funktionen aneinandergehängt. Durch das aneinanderhängen dieser Funktionen wird die API programmiert. Allgemein wichtig ist der HTTP input sowie der HTTP output. So können wir mit unserer "simulierten Webseite" kommunizieren. In der Konsole von Node-RED sollten wir auch Auslesen können falls jemand unsere Webseite aufgerufen hat. Im Allgemeinen sollten wir auch nichts ausser dem Statuscode 200 von dieser "Webseite" erhalten. Dadurch wissen wir auch, dass alles funktioniert. Falls die Webseite nun auch eine Funktion haben soll kann man diese zwischen dem In und Output einfügen. Diese Funktion können wir nun mit Java script Code füttern um unserer API eine Funktion zu geben. 


