#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    #It will print out the input the user types and exit.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.request[0].encode())
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

