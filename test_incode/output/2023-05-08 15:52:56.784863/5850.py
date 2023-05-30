#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them in a
    #browser
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = os.path.join(self.server.root, self.path)
            if os.path.isfile(path):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(open(path).read())
            else:
                self.send_error(404)
    
    server = HTTPServer(('localhost', 8000), Handler)
    server.serve_forever()

