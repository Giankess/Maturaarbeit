import requestparser
class responsebau:
    def Getresponse(self):
        try:
            f = open(path)
            print(Version 200 OK
            Date: time.strftime(%a, %d %b %Y %H: %M: %S %Z)
            Host: Requestinhalt["Host"]
            Server: Python
            Accept-Ranges: bytes
            Content - Lenght: f.size
            Content-Type: text/plain
            f.read())
        except FileNotFoundError:
            #auf error-methoden umschalten wenn der Pfad nicht gefunden wird
            Errorresponse()
    def Putresponse(self):
        f = open(path, w)
        f.write(Body)
        #response erstellen
        print(Version 201 Created
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Host: Requestinhalt["Host"]
        Server: Python
        Accept - Ranges: bytes
        Content - Lenght: f.size
        Content - Type: text/html
        f.read())
    def Errorresponse(self:
        #Error bei nicht gefundener Datei
        print(Version 404 Not Found
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Server: Python
        Host: Requestinhalt[Host]
        )
    def Errorresponse1(self):
        #Error bei unbekannter Methode
        print(Version 501 Not Implemented
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Server: Python
        Host: Requestinhalt[Host]
        )
