from ResponseBuilder import *
class SwitchMethod:
    def Switch(self,ps):
        rb = ResponseBuilder()
        if ps.Method == "GET":
            response = rb.Getresponse(ps)
        elif ps.Method == "PUT":
            response = rb.Putresponse(ps)
        else:
            response = rb.Errorresponse(ps)
        return response
