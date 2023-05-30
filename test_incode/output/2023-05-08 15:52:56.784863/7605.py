#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    web = HTTPServer(("localhost", 80), SimpleHTTPRequestHandler)
    web.serve_forever()

