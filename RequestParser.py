class RequestParser:
    def Parse(self,request):
        #Erhaltene Request lokal als String abspeichern
        string = request
        # string in Zeilen spalten
        zeilen = string.split('\r\n')
        #Dictionary erstellen
        self.Requestinhalt = {}
        #Variablen definieren
        self.Body = ""
        self.Method = ""
        self.Version = ""
        self.Requestinhalt['Host'] = "localhost:8000"
        #alle Zeilen Parsen
        for zeile in zeilen:
            if ":" in zeile:
                #Zeilen aus dem Header haben einen :
                parts = zeile.split(': ')
                self.Requestinhalt[parts[0]]=parts[1]
            elif "HTTP" in zeile:
                #erste Zeile enthält http
                parts = zeile.split(' ')
                self.Method = parts[0]
                self.Path = parts[1]
                if self.Path == "/":
                    self.Path = "./index.html"
                else:
                    self.Path = "."+self.Path
                self.Version = parts[2]
            else:
                #der Rest ist vom Body
                self.Body += zeile
        #Kodierung in der Request suchen und abspeichern
        if "Content-Type" in string:
            if "charset" in self.Requestinhalt['Content-Type']:
                self.contenttype = self.Requestinhalt['Content-Type'].split('charset=')
                self.code = string(self.contenttype[1])
            else:
                self.code = "utf-8"
        else:
            self.code = "utf-8"
            self.Requestinhalt['Content-Type'] = "undefined"
