class requestparser:
    def parse(self):
        string = self.request
        # string in Zeilen spalten
        zeilen = string.split('
                              ')
        # erste Zeile spalten und Variablen entnehmen
        zeile1 = zeilen[1]
        parts1 = zeile1.split(' ')
        Method = parts1[1]
        Path = parts1[2]
        Version = parts[3]
        # restliche Zeilen Spalten
        zeile2 = zeilen[2]
        parts2 = zeile2.split(':')
        zeile3 = zeilen[3]
        parts3 = zeile3.split(':')
        zeile4 = zeilen[4]
        parts4 = zeile[4].split(':'))
        Requestinhalt = {parts2[1] : parts2[2], {parts3[1] : parts3[2], {parts4[1] : parts4[2]}

        #loop-versuch
        for i in zeilen[]:
            'zeile'i = zeilen[i]
            'parts'i= 'zeile'i.split(':')
            Requestinhalt1 = {'parts'i[1] : 'parts'i[2]}
