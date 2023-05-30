#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes("""
            <html>
            <head>
            <title>Hello World</title>
            </head>
            <body>
            <h1>Hello World</h1>
            <p>%s</p>
            </body>
            </html>
            """ % '\n'.join(words),"utf8"))
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting httpd on', server_address)
    httpd.serve_forever()

