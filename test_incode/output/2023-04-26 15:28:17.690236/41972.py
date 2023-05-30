#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write('<html><body>')
            self.wfile.write('<h1>Fruits</h1>')
            self.wfile.write('<ul>')
            
            for fruit in ['apple', 'banana', 'cherry']:
                self.wfile.write('<li>' + fruit + '</li>')
            
            self.wfile.write('</ul></body></html>')
    
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()
    
