#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import os
    import sys
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                path = "index.html"
            
            path = os.path.join(os.path.dirname(__file__), path)
            
            file = open(path, "r")
            html = file.read()
            file.close()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html)
    
    server = HTTPServer(('', 8000), FruitHandler)
    
    server.serve_forever()

