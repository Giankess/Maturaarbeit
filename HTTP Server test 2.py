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
        string = 'requestinhalt'
        a = string.split('
                         ')
        b = a[1]
        c = b.split(' ')
        Method = c[1]
        Path = c[2]
        d = a[2]
        e = d.split(':')
        UserAgent = e[2]
        f = a[3]
        g = f.split(':')
        Host = g[2]
        
        
        
        
            
#Objekt Handler benutzt Methoden, etc. der Klasse MyHandler
Handler = MyHandler()

httpd = socketserver.TCPServer(("", PORT), Handler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

