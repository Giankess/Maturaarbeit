import http.server
import socketserver
import os
#Bibliotheken importieren

PORT = 8000
#Port festlegen

Handler = http.server.SimpleHTTPRequestHandler
#Handler festlegen, welcher Anfragen bearbeitet<-Ersetzen
#Start Konstruktor
class MyHandler:
    #Allgemeine Variablen für den Handler kommen hier rein
    def Handle(self):
    #String spalten um Methode etc. zu bekommen
        string = self.request
    #string in Zeilen spalten
        a = string.split('
                         ')
    #erste Zeile spalten und Variablen entnehmen
        b = a[1]
        c = b.split(' ')
        Method = c[1]
        Path = c[2]
    #zweite Zeile spalten
        d = a[2]
        e = d.split(':')
        UserAgent = e[2]
    #Dritte Zeile spalten
        f = a[3]
        g = f.split(':')
        Host = g[2]
    #Methode testens
        if Method == "GET":
        #GET Methode verwenden
            #testfunktion ob file existiert
            print(c[3] 200 OK
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

