from ResponseBuilder import *
class TestMethod:
    def TestMethode(self,ps):
        rb = ResponseBuilder()
        if ps.Method == "GET":
            response = rb.Getresponse(ps)
        elif ps.Method == "PUT":
            response = rb.Putresponse(ps)
        else:
            response = rb.Errorresponse(ps)
        return response
