#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that enumerates a port.
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()

