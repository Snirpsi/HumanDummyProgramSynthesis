#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A handler for requests to fruits. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write('<html><head><title>Fruits</title></head>')
            self.wfile.write('<body><h1>Fruits</h1>')
            
            for fruit in ['apple', 'banana', 'cherry']:
                self.wfile.write('<p>%s</p>' % fruit)
            
            self.wfile.write('</body></html>')
            
    httpd = HTTPServer(("", 80), FruitHandler)
    
    print("Serving at port 80")
    httpd.serve_forever()
    
