#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that adds a port.
    while True:
        port = port + 1
        server = HTTPServer(('', port), SimpleHTTPRequestHandler)
        server.serve_forever()

