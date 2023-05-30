#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that returns all ports.
    server = HTTPServer(("", ports[0]), SimpleHTTPRequestHandler)
    server.serve_forever()

