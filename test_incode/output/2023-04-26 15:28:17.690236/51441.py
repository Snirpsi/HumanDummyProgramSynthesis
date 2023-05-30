#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and prints a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><head><title>Word Converter</title></head>'
                                    '<body><p>Word Converter</p>'
                                    '<form action="/convert" method="post">'
                                    '<input name="word" type="text"/>'
                                    '<input name="port" type="text"/>'
                                    '<input name="submit" type="submit" value="Convert"/>'
                                    '</form></body></html>', 'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting server on port 8080')
    httpd.serve_forever()
