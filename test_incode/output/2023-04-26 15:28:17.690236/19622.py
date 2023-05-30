#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Enumerate Words</title></head>'
                '<body><p>Enumerate Words</p>'
                '<form action="/" method="GET">'
                '<input type="text" name="word"/>'
                '<input type="submit" value="Enumerate"/>'
                '</form></body></html>'
                )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting server')
    httpd.serve_forever()
    
