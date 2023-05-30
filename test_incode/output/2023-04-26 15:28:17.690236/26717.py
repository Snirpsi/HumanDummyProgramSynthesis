#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or opens all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.words())
            else:
                self.send_response(404)
                self.end_headers()
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpd on port 8000...')
    httpd.serve_forever()
    
