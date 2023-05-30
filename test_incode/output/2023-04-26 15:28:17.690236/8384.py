#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            path = urllib.parse.unquote(self.path)
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body>', 'utf-8'))
                self.wfile.write(bytes('<h1>Hello World!</h1>', 'utf-8'))
                self.wfile.write(bytes('</body></html>', 'utf-8'))
            elif path == '/multiply':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes('<html><body>', 'utf-8'))
                self.wfile.write(bytes('<h1>Hello World!</h1>', 'utf-8'))
                self.wfile.write(bytes('</body></html>', 'utf-8'))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting httpd...')
    httpd.serve_forever()
