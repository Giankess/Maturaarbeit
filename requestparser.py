class requestparser:
    def parse(self):
        string = self.request
        # string in Zeilen spalten
        zeilen = string.split(\n)
        # erste Zeile spalten und Variablen entnehmen
        zeile1 = zeilen[0]
        parts1 = zeile1.split(' ')
        Method = parts1[0]
        Path = parts1[1]
        Version = parts[2]
        zeilen = zeilen - zeilen[0]
        i = 0
        while zeile != "":
            for zeile in zeilen[]:
                parts = zeile.split(:)
                Requestinhalt = {}
                Requestinhalt[parts[0]]=parts[1]
                i=i+1
        Body = ""
        while zeile != "":
            i=i+1
            Body = Body+zeile[i]