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
        catch:
            #auf error-methoden umschalten
            Errorresponse()
    def Putresponse(self):
        f = open(path, w)
        #was schreiben? beim parser nicht sortiert für dictionary
        f.write()


