import http.server
import socketserver
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
        def Parcer():
            string = request
            string.split(' ')



httpd = socketserver.TCPServer(("", PORT), Handler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

