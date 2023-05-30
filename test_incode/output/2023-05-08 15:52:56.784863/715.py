#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(words))
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    server_thread = ThreadingMixIn(httpd.sockets)
    server_thread.start()
    
    httpd.serve_forever()

