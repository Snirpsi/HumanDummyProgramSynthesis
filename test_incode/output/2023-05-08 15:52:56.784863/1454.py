#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that converts a http request.
    http_server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    http_server.serve_forever()

