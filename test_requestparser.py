from requestparser import parse
testrequest = """POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: application/x-www-form-urlencoded
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

licenseID=string&content=string&/paramsXML=string"""

parse(testrequest)
print(Version)
print(Method)
print(Path)
print("Host: ", Requestinhalt['User-Agent'])
print(Body)
