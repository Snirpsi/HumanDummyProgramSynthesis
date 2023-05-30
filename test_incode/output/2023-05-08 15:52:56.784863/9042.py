#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    httpd = HTTPServer(('localhost', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()

