from ResponseBuilder import *
class SwitchMethod:
    def Switch(self,ps):
        #Objekt vom ResponseBuilder erstellen
        rb = ResponseBuilder()
        #Auf verwendete Methode testen und entsprechende ResponseBuilder-Methode aufrufen
        if ps.Method == "GET":
            response = rb.Getresponse(ps)
        elif ps.Method == "PUT":
            response = rb.Putresponse(ps)
        else:
            response = rb.Errorresponse(ps)
        #Vom ResponseBuilder erstellte Response an MainDatei weitergeben
        return response
