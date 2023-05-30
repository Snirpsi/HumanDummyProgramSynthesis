#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Wordlist</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<h1>Wordlist</h1>')
            self.wfile.write(b'<ol>')
            for word in wordlist:
                self.wfile.write(b'<li>' + word + '</li>')
            self.wfile.write(b'</ol>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()
    
