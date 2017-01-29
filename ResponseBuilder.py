import time
import os
import codecs
class ResponseBuilder:
    #Vorlagen für die Response abspeichern
    vorlage = ("{version} {sc}"+'\r\n'+"Date: {date}"+'\r\n'+"Server: Python"+'\r\n'+"Host: {host}"+'\r\n'+"{rest}"+'\r\n')
    vorlage2 = ("Accept-Ranges: bytes"+'\r\n'+"Content - Lenght: {size}"+'\r\n'+"Content-Type: {contenttype}"+'\r\n')
    #Einzelne Response Methoden
    def Getresponse(self, ps):
        try:
            #Response erstellen
            response = self.vorlage.format(version = ps.Version, sc = "200 OK", date =\
                time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.vorlage2.format(size = os.path.getsize(ps.Path), contenttype = ps.Requestinhalt['Content-Type']))
            #File dekodieren und öffnen
            with codecs.open(os.path.abspath(ps.Path),'r', encoding= ps.code) as f:
                myfile = f.read()
            response += myfile
            #Response and TestMethod weitergeben
            return response
        except FileNotFoundError:
            #auf error-methoden umschalten wenn der Pfad nicht gefunden wird
            request = self.Errorresponse(ps)
            return request
    def Putresponse(self, ps):
        #response erstellen
        response = self.vorlage.format(version = ps.Version, sc = "201 Created", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.vorlage2.format(size = os.path.getsize(ps.Path), contenttype = ps.Requestinhalt['Content-Type']))
        # File dekodieren und öffnen
        with codecs.open(os.path.abspath(ps.Path), 'r', encoding= ps.code) as f:
            myfile = f.write(ps.body)
        response += myfile
        # Response and TestMethod weitergeben
        return response

    # Error bei nicht gefundener Datei
    def Errorresponse(self, ps):
        #Response erstellen
        response = self.vorlage.format(version = ps.Version, sc = "404 Not Found", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """
<html><head><title>Not Found</title></head><body>
Sorry, the object you requested was not found.
</body><html>""")
        # Response and TestMethod weitergeben
        return response

    # Error bei unbekannter Methode
    def Errorresponse1(self, ps):
        #Response erstellen
        response = self.vorlage.format(version = ps.Version, sc = "501 Not Implemented", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """
<html><head><title>Not Found</title></head><body>
Sorry, the object you requested was not found.
</body><html>""")
        # Response and TestMethod weitergeben
        return response


