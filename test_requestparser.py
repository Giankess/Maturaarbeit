import requestparser
testrequest = """POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: application/x-www-form-urlencoded
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

licenseID=string&content=string&/paramsXML=string"""
string = testrequest
# string in Zeilen spalten
zeilen = string.split('\n')

Requestinhalt = {}
Body = ""
#alle Zeilen Parsen
for zeile in zeilen:
    if ": " in zeile:
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
        Body = Body+zeile
print(Version)
print(Method)
print(Path)
print("Host: ", Requestinhalt['User-Agent'])
print(Body)
