#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers or enumerates a port. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Hello World!</h1>')
            else:
                self.send_response(404)
                self.end_headers()
                return
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving at http://127.0.0.1:8000/')
    httpd.serve_forever()
