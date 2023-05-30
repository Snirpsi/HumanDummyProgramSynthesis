#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or stores a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            path = self.path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>My Webserver</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>My Webserver</h1>')
                self.wfile.write(b'<p>')
                self.wfile.write(b'<i>')
                self.wfile.write(b'My webserver')
                self.wfile.write(b'</i><br/>')
                self.wfile.write(b'</body></html>')
            elif path == '/port':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>My Webserver</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>My Webserver</h1>')
                self.wfile.write(b'<p>')
                self.wfile.write(b'<i>')
                self.wfile.write(b'My webserver')
                self.wfile.write(b'</i><br/>')
                self.wfile.write(b'<p>')
                self.wfile.write(b'<i>')
                self.wfile.write(b'Port')
                self.wfile.write(b'</i><br/>')
                self.wfile.write(b'</body></html>')
            elif path == '/words':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>My Webserver</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>My Webserver</h1>')
                self.wfile.write(b'<p>')
                self.wfile.write(b'<i>')
                self.wfile.write(b'My webserver')
                self.wfile.write(b'</i><br/>')
                self.wfile.write(b'<p>')
                self.wfile.write(b'<i>')
                self.wfile.write(b'Words')
                self.wfile.write(b'</i><br/>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()
    
