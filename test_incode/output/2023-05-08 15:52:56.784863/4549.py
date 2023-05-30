#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that enumerates numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

