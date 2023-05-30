#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>Enumerate Input</title></head>')
            self.wfile.write('<body>')
            self.wfile.write('<textarea id="input"></textarea>')
            self.wfile.write('</body></html>')
    
    server = HTTPServer(("", 80), Handler)
    server.serve_forever()
    
