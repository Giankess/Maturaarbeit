import requestparser.py
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
            #rest der Get-Methode
        except FileNotFoundError:
            #auf error-methoden umschalten
            Errorresponse1()
    def Putresponse(self):
        f = open(path, w)
        #was schreiben? beim parser nicht sortiert für dictionary
        f.write(Body)
        #respnse erstellen
        print(Version 201 Created
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Host: Requestinhalt["Host"]
        Server: Python
        Accept - Ranges: bytes
        Content - Lenght: f.size
        Content - Type: text/html
        f.read())
    def Errorresponse(self:
        print(Version 404 Not Found
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Server: Python
        Host: Requestinhalt[Host]
        )
    def Errorresponse1(self):
        print(Version 501 Not Implemented
        Date: time.strftime( %a, %d %b %Y %H: %M: %S %Z)
        Server: Python
        Host: Requestinhalt[Host]
        )
