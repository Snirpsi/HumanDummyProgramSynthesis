#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in fruirs.html
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open('fruirs.html').read())
    
    server = HTTPServer(('localhost', 8080), FruitHandler)
    server.serve_forever()

