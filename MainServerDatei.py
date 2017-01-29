import socketserver
import os
from RequestParser import *
from TestMethod import *
#Bibliotheken importieren

PORT = 8000
#Port festlegen
#Start Konstruktor
class MyHandler(socketserver.BaseRequestHandler):
    #Meine Handler Methode
    def handle(self):
        #Objekte erstellen
        ps = RequestParser()
        tm = SwitchMethod()
        #Request abspeichern
        request = b''
        while b'\r\n\r\n' not in request:
            data = self.request.recv(1024)
            if not data:
                break
            request += data
        #Request dekodieren
        request = request.decode("UTF-8")
        print(request)
        #Request parsen
        ps.Parse(request)
        #Request erstellen und abspeichern
        self.response = ""
        self.response += tm.Switch(ps)
        print(self.response)
        #Response kodieren
        self.response = self.response.encode('utf-8')
        #Response absenden
        self.request.sendall(self.response)

#festlegen, worüber der Server läuft
httpd = socketserver.TCPServer(("localhost", PORT), MyHandler)

#Nachricht dass der Server über Port 8000 läuft
print("serving at port", PORT)

#Lässt Server laufen, bis das Programm beendet wird
httpd.serve_forever()


