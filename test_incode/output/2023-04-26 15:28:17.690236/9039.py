#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socket

    class WordHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Enumerate Words</title></head><body>')
                self.wfile.write(b'<h1>Enumerate Words</h1>')
                self.wfile.write(b'<p>This program enumerates words in a text file.</p>')
                self.wfile.write(b'<p>The program is written using Python 3.</p>')
                self.wfile.write(b'</body></html>')
            elif path == '/words':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Enumerate Words</title></head><body>')
                self.wfile.write(b'<h1>Enumerate Words</h1>')
                self.wfile.write(b'<p>This program enumerates words in a text file.</p>')
                self.wfile.write(b'<p>The program is written using Python 3.</p>')
                self.wfile.write(b'</body></html>')
            elif path == '/words/<word>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Enumerate Words</title></head><body>')
                self.wfile.write(b'<h1>Enumerate Words</h1>')
                self.wfile.write(b'<p>This program enumerates words in a text file.</p>')
                self.wfile.write(b'<p>The program is written using Python 3.</p>')
                self.wfile.write(b'</body></html>')
            elif path == '/words/<word>/<count>':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Enumerate Words</title></head><body>')
                self.wfile.write(b'<h1>Enumerate Words</h1>')
                self.wfile.write(b'<p>This program enumerates words in a text file.</p>')
                self.wfile.write(b'<p>The program is written using Python 3.</p>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, WordHandler)
    print('Starting httpd on port 8000.')
    httpd.serve_forever()
</code>
<|/ a dscore=0 tags=python,webserver,python-3.x |>
