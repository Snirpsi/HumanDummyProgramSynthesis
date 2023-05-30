#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse
    from socketserver import ThreadingMixIn

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Hello, world!")
            elif path == '/words':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"word1, word2, word3".encode('utf-8'))
            elif path == '/words/?word=word1':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"word1".encode('utf-8'))
            elif path == '/words/?word=word2':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"word2".encode('utf-8'))
            elif path == '/words/?word=word3':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"word3".encode('utf-8'))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    ThreadingMixIn.