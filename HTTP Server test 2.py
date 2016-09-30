import http.server
import socketserver
#Bibliotheken importieren

PORT = 8000
#Port festlegen

Handler = http.server.SimpleHTTPRequestHandler
#Handler festlegen, welcher Anfragen bearbeitet

httpd = socketserver.TCPServer(("", PORT), Handler)
#festlegen, worüber der Server läuft

print("serving at port", PORT)
#NAchricht dass der Server über Port 8000 läuft

httpd.serve_forever()
#Lässt Server laufen, bis das Programm beendet wird

