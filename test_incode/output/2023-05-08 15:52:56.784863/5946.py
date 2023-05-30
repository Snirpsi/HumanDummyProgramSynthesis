#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that prints a http request.
    webserver = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    webserver.serve_forever()

