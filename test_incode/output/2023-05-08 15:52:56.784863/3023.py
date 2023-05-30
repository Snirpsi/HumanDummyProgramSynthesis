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
            
            html = ""
            for word in words:
                html += f"<p>{word}</p>"
            self.wfile.write(bytes(html, 'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting server')
    httpd.serve_forever()

