import time
import os
import codecs
class ResponseBuilder:
    vorlage = ("""{version} {sc}
        Date: {date}
        Server: Python
        Host: {host}
        {rest}
        """)
    vorlage2 = """Accept-Ranges: bytes
        Content - Lenght: {size}
        Content-Type: {contenttype}
        """
    def Getresponse(self, ps):
        try:
            response = self.vorlage.format(version = ps.Version, sc = "200 OK", date =\
                time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.vorlage2.format(size = os.path.getsize(ps.Path), contenttype = ps.Requestinhalt['Content-Type']))
            with codecs.open(os.path.abspath(ps.Path),'r', encoding= ps.code) as f:
                myfile = f.read()
            response += myfile
            return response
        except FileNotFoundError:
            #auf error-methoden umschalten wenn der Pfad nicht gefunden wird
            request = self.Errorresponse(ps)
            return request
    def Putresponse(self, ps):
        #response erstellen
        response = self.vorlage.format(version = ps.Version, sc = "201 Created", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.vorlage2.format(size = os.path.getsize(ps.Path), contenttype = ps.Requestinhalt['Content-Type']))
        with codecs.open(os.path.abspath(ps.Path), 'r', encoding= ps.code) as f:
            myfile = f.write(ps.body)
        response += myfile
        return response
    def Errorresponse(self, ps):
        #Error bei nicht gefundener Datei
        response = self.vorlage.format(version = ps.Version, sc = "404 Not Found", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """
            <html><head><title>Not Found</title></head><body>
            Sorry, the object you requested was not found.
            </body><html>""")
        return response
    def Errorresponse1(self, ps):
        #Error bei unbekannter Methode
        response = self.vorlage.format(version = ps.Version, sc = "501 Not Implemented", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """
            <html><head><title>Not Found</title></head><body>
            Sorry, the object you requested was not found.
            </body><html>""")
        return response


