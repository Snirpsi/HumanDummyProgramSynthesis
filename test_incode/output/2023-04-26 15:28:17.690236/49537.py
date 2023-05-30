#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or converts numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            path = self.path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers/<int:num>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers/<int:num>/<int:num>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers/<int:num>/<int:num>/<int:num>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers/<int:num>/<int:num>/<int:num>/<int:num>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers</h1></center>')
                self.wfile.write(b'</body></html>')
            elif path == '/numbers/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>List of numbers