Funktionsweise Server-Client Modell

Funktionsweise und Aufgaben einer API
HTTP Methoden GET, POST, PUT, DELETE
Funktionsweise eines simplen Web-Servers
Protokolle
Was ist ein Protokoll?
Erstellen eines Protokolls für eine einfache Aufgabe mit Sequenz- und Zustandsdiagrammen
Schichtenmodell
TCP-IP Stack
Auf jeder Schicht die zentralen Protokolle kennen und erklären können
Anwendungsschicht
HTTP
DNS
DHCP
Ports
Transportschicht
TCP
UDP
Vermittlungsschicht/Internetschicht
IP
Aufbau einer IP-Adresse
Subnetzmasken
Subnetze
Private und öffentliche IP-Adressen kennen
Berechnung der Anzahl Netzwerke und Hosts mit der Subnetzmaske
Physikalische Schicht/Netzzugangsschicht
ARP
Aufbau eines IP-Frame
Aufbau eines Ethernet-Frames
Aufbau einer MAC-Adresse






## Routing

Switch vs. Router

**Router**   
Ist dafür gemacht Datenverkehr zwischen Netzwerken zu Bearbeiten 
Ist ein Knotenpunkt für Datenfilterungen  
**Switch**  
Ist dafür gemacht Datenverkehr zwischen einzenlnen Geräten zu Bearbeiten 

Ablauf ARP
Switch- und Routing-Tabellen lesen und verstehen
Routing-Tabellen erstellen
Netzwerke konfigurieren
Standardgateway
NAT
Aufgaben von NAT
Hole Punching









Eine Nachricht ist zunächst einfach ein Abfolge von Bytes. Üblicherweise werden diese Bytes in drei Teile aufgeteilt:

**Header**
Der Header enthält Informationen, welche für das Protokoll von Bedeutung sind, z.B. Absenderadresse und Zieladresse einer Nachricht.
**Payload**
Die Payload umfasst den Teil einer Nachricht, welcher für das Protokoll zu welchem die Nachricht gehört, nicht relevant ist. Die Payload bietet die Möglichkeit, Informationen zu transportieren, welche dann auf einer höheren Ebene von Bedeutung sind.
**Trailer**
Der Trailer ist wiederum Teil des Protokolls, zu welchem die Nachricht gehört. Er enthält zum Beispiel Informationen, zur Überprüfung, ob die Nachricht vollständig und korrekt übertragen wurde (z.B. Quersummen über alle Bytes der Nachricht).



**DHCP**
Dynamic Host Configuration Protocol 
Automatische vergabe und neuvergabe von IP-Adressen in einem Netzwerk durch einen Server. 

Geroutet werden kann auch manuell, ist aber zeitaufwändig. Hat aber den Vorteil, dass spezifische Einstellungen für spezifische Devices innnerhalb eines Netzwerkes vorgenommen werden können. 

**DNS**
Domain Name System 
Protokoll zur umwandlung von IP Adressen in Namentliche Adressen. 1.232.42.17 -> Youtube.com 

**ARP**
Ist das Protokoll, welches nach MAC-Adressen sucht, indem es einen Brodchast in Lokalen Netzwerk mit der IP des gewünschten Gerätes sendet, und so antwort von dem Gerät mit der gewünschten IP-Adresse erhält.


**MAC-Adresse**
Die Adresse deines Hardware Gerätes. Diese wird mit der IP-Adresse immer auch vor einem Datenaustausch benötigt, um sichserzustellen, dass es sich auch um dasselbe gerät handelt, wenn ein Gerät eine Spezifische IP-Adresse in einem Netzwerk hat. Ist im Zusammenhang mit DHCP noch wichtig, da man sonst die Daten von dem Vorherigen IP-Besitzer erhalten würde. 
