import http.server
import socketserver
import os
import requestparser.py
import Testmethode.py
#Bibliotheken importieren

PORT = 8000
#Port festlegen

Handler = MyHandler.Handle(self)
#Handler festlegen, welcher Anfragen bearbeitet<-Ersetzen
#Start Konstruktor
class MyHandler:
    #Allgemeine Variablen für den Handler kommen hier rein
    def Handle(self):
    parse(self)
    Testmethode(self)
        
            
#Objekt Handler benutzt Methoden, etc. der Klasse MyHandler
Handler = MyHandler()

httpd = socketserver.TCPServer((Host, PORT), MyHandler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

