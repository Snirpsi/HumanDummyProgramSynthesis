#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import StringIO
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                content = 'Hello World!'
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            else:
                self.send_error(404)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

