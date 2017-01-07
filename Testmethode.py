from responsebau import *
class Testmethode:
    def Testmethode(self,ps):
        rb = responsebau()
        if ps.Method == "GET":
            response = rb.Getresponse(ps)
        elif ps.Method == "PUT":
            response = rb.Putresponse(ps)
        else:
            response = rb.Errorresponse(ps)
        return response
