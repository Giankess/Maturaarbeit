import http.server
import socketserver
import os
import requestparser
import Testmethode
#Bibliotheken importieren

PORT = 8000
#Port festlegen

Handler = MyHandler.Handle(self)
#Handler festlegen, welcher Anfragen bearbeitet<-Ersetzen
#Start Konstruktor
class MyHandler:
    #Allgemeine Variablen für den Handler kommen hier rein
    def Handle(self):
        while True:
            data += self.request.recv()
            if not data:
                break
            request += data
        parse(request)
        Testmethode(Method)
        
            
#Objekt Handler benutzt Methoden, etc. der Klasse MyHandler
Handler = MyHandler()

httpd = socketserver.TCPServer((Host, PORT), MyHandler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

