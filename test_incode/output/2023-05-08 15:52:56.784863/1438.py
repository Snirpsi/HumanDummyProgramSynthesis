#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them in HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('fruits.txt', 'r') as f:
                self.wfile.write(f.read())
    
    httpd = HTTPServer(('', 8080), Handler)
    print('Serving at http://127.0.0.1:8080')
    httpd.serve_forever()

