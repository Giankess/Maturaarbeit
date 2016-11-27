import http.server
import socketserver
import os
#Bibliotheken importieren

PORT = 8000
#Port festlegen

Handler = MyHandler.Handle(self)
#Handler festlegen, welcher Anfragen bearbeitet<-Ersetzen
#Start Konstruktor
class MyHandler:
    #Allgemeine Variablen für den Handler kommen hier rein
    def Handle(self):
    #String spalten um Methode etc. zu bekommen
        string = self.request
    #string in Zeilen spalten
        zeilen = string.split('
                         ')
    #erste Zeile spalten und Variablen entnehmen
        zeile1 = zeilen[1]
        parts1 = zeile1.split(' ')
        Method = parts1[1]
        Path = parts1[2]
    #zweite Zeile spalten
        zeile2 = zeilen[2]
        parts2 = zeile2.split(':')
        UserAgent = parts2[2]
    #Dritte Zeile spalten
        zeile3 = zeilen[3]
        parts3 = zeile3.split(':')
        Host = parts3[2]
    #Methode testens
        if Method == "GET":
        #GET Methode verwenden
            #testfunktion ob file existiert
            print(parts1[3] 200 OK
    Date: time.strftime(%a, %d %b %Y %H:%M:%S %Z)
    Server: Apache
    ...
    Content-Lenght:
    ...
    file Inhalt)
        elif Method == "POST":
        #POST Methode verwenden
            # testfunktion ob file existiert

        else:
        #ERROR senden
        
        
            
#Objekt Handler benutzt Methoden, etc. der Klasse MyHandler
Handler = MyHandler()

httpd = socketserver.TCPServer((Host, PORT), MyHandler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

