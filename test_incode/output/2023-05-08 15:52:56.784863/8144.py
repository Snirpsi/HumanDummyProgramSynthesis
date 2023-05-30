#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that converts fruits.txt into HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.normpath(self.path)
            if path == "/":
                path = "index.html"
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open(path).read())
    
    server = HTTPServer(('localhost', 8080), RequestHandler)
    server.serve_forever()

