#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that converts ports.
    from http.server import HTTPServer, BaseHTTPRequestHandler
    httpd = HTTPServer(('', 0), BaseHTTPRequestHandler)
    for port in ports:
        httpd.serve_forever()

