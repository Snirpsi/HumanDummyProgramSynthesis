#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class WordHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Words</h1>')
                self.wfile.write(b'<ul>')
                self.wfile.write(b'<li>')
                self.wfile.write(b'<a href="/">Home</a>')
                self.wfile.write(b'</li>')
                self.wfile.write(b'<li>')
                self.wfile.write(b'<a href="/add">Add</a>')
                self.wfile.write(b'</li>')
                self.wfile.write(b'</ul>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
        
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, WordHandler)
    