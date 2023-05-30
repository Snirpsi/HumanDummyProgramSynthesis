#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that converts ports.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    httpd = HTTPServer(("", ports[0]), MyHandler)
    print("Serving at port", ports[0])
    httpd.serve_forever()

