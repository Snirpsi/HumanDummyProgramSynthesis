#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that iterates over all ports.
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    server.serve_forever()

