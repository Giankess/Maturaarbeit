import time
class ResponseBuilder:
    Vorlage = ("""{version} {sc}
        Date: {date}
        Server: Python
        Host: {host}
        {rest}""")
    Vorlage2 = """Accept-Ranges: bytes
            Content - Lenght: {size}
            Content-Type: {contenttype}
            """
    def Getresponse(self, ps):
        try:
            f = open(ps.Path)
            response = self.Vorlage.format(version = ps.Version, sc = "200 OK", date =\
                time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.Vorlage2.format(size = f.size, contenttype = ps.Requestinhalt['Content-Type']))
            file = f.read()
            file = file.encode("'",ps.code,"'")
            response = response.encode("UTF-8")
            response += file
            return response
        except FileNotFoundError:
            #auf error-methoden umschalten wenn der Pfad nicht gefunden wird
            request = self.Errorresponse(ps)
            return request
    def Putresponse(self, ps):
        f = open(ps.Path, w)
        f.write(Body)
        #response erstellen
        response = self.Vorlage.format(version = ps.Version, sc = "201 Created", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = self.Vorlage2.format(size = ps.f.size, contenttype = ps.Requestinhalt['Content-Type']))
        file = ps.f.read()
        file = file.encode("'",ps.code,"'")
        response = response.encode("UTF-8")
        response += file
        return response
    def Errorresponse(self, ps):
        #Error bei nicht gefundener Datei
        response = self.Vorlage.format(version = ps.Version, sc = "404 Not Found", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """<html><head><title>Not Found</title></head><body>
Sorry, the object you requested was not found.
</body><html>""")
        response = response.encode("UTF-8")
        return response
    def Errorresponse1(self, ps):
        #Error bei unbekannter Methode
        response = self.Vorlage.format(version = ps.Version, sc = "501 Not Implemented", date =\
            time.strftime("%a, %d %b %Y %H:%M:%S %Z"), host = ps.Requestinhalt['Host'],rest = """<html><head><title>Not Found</title></head><body>
Sorry, the object you requested was not found.
</body><html>""")
        response = response.encode("UTF-8")
        return response

