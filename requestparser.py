class requestparser:
    def parse(self):
        #string = self.request
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
        for zeile in zeilen:
            if ":" in zeile:
                parts = zeile.split(':')
                Requestinhalt[parts[0]]=parts[1]
            elif "HTTP" in zeile:
                parts = zeile.split(' ')
                Method = parts[0]
                Path = parts[1]
                Version = parts[2]
            else:
                Body = Body+zeile