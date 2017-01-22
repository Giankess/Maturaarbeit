import socketserver
import os
from RequestParser import *
from TestMethod import *
#Bibliotheken importieren

PORT = 8000
#Port festlegen
#Start Konstruktor
class httpHandler(socketserver.BaseRequestHandler):
    #Allgemeine Variablen für den Handler kommen hier rein
    def handle(self):
        ps = RequestParser()
        tm = SwitchMethod()
        request = b''
        while b'\r\n\r\n' not in request:
            data = self.request.recv(1024)
            if not data:
                break
            request += data
        request = request.decode("UTF-8")
        print(request)
        ps.Parse(request)
        response = b""
        response += tm.Switch(ps)
        print(response)
        self.request.sendall(response)

httpd = socketserver.TCPServer(("localhost", PORT), httpHandler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#Nachricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

