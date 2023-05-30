#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and prints fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruits)
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FruitHandler)
    print('Starting httpserver on port 8000...')
    httpd.serve_forever()
    
