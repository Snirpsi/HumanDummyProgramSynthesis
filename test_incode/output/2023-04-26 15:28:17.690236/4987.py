#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Serve the fruits. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            fruits = ['apple', 'banana', 'cherry']
            
            for fruit in fruits:
                self.wfile.write(fruit + '\n')
        
    httpd = HTTPServer(("", 8080), FruitHandler)
    print("Serving at port 8080")
    httpd.serve_forever()
    
