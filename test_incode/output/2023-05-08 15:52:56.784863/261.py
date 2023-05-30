#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that requests numbers.txt and prints them out
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(numbers)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

