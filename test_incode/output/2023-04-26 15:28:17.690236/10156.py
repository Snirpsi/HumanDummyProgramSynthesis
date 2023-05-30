#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""<html><body><h1>List of numbers</h1>
            <ul>
            """)
            for n in range(10):
                self.wfile.write(str(n) + "<br>")
            self.wfile.write("""</ul></body></html>""")
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()
