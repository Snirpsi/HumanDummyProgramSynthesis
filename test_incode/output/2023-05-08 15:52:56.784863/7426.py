#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from SocketServer import ThreadingUDPServer
    from socketserver import ThreadingTCPServer

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

