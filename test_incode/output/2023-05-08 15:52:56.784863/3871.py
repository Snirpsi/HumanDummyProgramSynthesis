#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.html and displays them.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(fruirs)
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting httpserver on port 8000')
    httpd.serve_forever()

