#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    httpd = BaseHTTPServer.HTTPServer(('',80), RequestHandler)
    httpd.serve_forever()

