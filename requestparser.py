class RequestParser:
    def Parse(self,request):
        string = request
        # string in Zeilen spalten
        zeilen = string.split('\n')
        self.Requestinhalt = {}
        self.Body = ""
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
        if "Content-Type" in string:
            if "charset" in self.Requestinhalt['Content-Type']:
                self.contenttype = Requestinhalt['Content-Type'].split('charset=')
                self.code = string(contenttype[1])
            else:
                self.code = "utf-8"
        else: self.code = "utf-8"
