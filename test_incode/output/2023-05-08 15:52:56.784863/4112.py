#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    #This example is for educational purposes only.
    #It is not intended to be used in a production environment.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers)
    
    server = HTTPServer(('', 8080), Handler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

