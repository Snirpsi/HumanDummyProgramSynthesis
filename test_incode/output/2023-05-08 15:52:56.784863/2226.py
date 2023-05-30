#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    webserver = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    webserver.serve_forever()

