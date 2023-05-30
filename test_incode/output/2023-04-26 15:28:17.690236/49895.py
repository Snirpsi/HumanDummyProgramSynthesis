#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and adds fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><body>')
            self.wfile.write('<h1>Fruits</h1>')
            self.wfile.write('</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Serving HTTP on port 8080...')
    httpd.serve_forever()
    
