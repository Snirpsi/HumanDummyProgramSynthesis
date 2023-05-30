#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and opens fruits. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruits)
    
    httpd = HTTPServer(('localhost', 8080), FruitHandler)
    httpd.serve_forever()
    
