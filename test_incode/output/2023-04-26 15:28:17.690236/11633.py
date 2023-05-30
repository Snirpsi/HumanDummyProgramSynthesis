#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request with a list of ports. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><body>')
            for port in range(1024):
                self.wfile.write('<p>Port %d: <a href="/">%s</a></p>\n' % (port, port+1))
            self.wfile.write('</body></html>')
    
    httpd = HTTPServer(("", 0), Handler)
    httpd.serve_forever()

<|/ file filename=server.py |>