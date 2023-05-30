#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that prints a http request.
    server = HTTPServer((url, 80), SimpleHTTPRequestHandler)
    server.serve_forever()

