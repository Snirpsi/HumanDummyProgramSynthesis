#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port. """    
    from http.server import HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse, parse_qs
    from sys import argv

    HOST, PORT = argv

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, ThreadingMixIn)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>