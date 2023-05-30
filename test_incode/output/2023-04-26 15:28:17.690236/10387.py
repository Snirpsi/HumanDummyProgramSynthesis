#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><head><title>Enumerate input</title></head>'
                                    '<body><p>Enumerate input</p>'
                                    '<form action="/" method="post">'
                                    '<input type="text" name="user_input">'
                                    '<input type="submit" value="Enumerate">'
                                    '</form></body></html>', 'UTF-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving HTTP on port 8080...')
    httpd.serve_forever()
    
