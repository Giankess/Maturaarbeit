class requestparser:
    def parse(request):
        string = request
        # string in Zeilen spalten
        zeilen = string.split('\n')
        # erste Zeile spalten und Variablen entnehmen
        #zeile1 = zeilen[0]
        #parts1 = zeile1.split(' ')
        #Method = parts1[0]
        #Path = parts1[1]
        #Version = parts[2]
        Requestinhalt = {}
        Body = ""
        #alle Zeilen Parsen
        for zeile in zeilen:
            if ":" in zeile:
                #Zeilen aus dem Header haben einen :
                parts = zeile.split(': ')
                Requestinhalt[parts[0]]=parts[1]
            elif "HTTP" in zeile:
                #erste Zeile enthält http
                parts = zeile.split(' ')
                Method = parts[0]
                Path = parts[1]
                Version = parts[2]
            else:
                #der Rest ist vom Body
                Body += zeile