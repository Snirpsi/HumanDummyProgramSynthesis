#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    server_address = ('localhost', 8000)
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing all content. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            for word in self.server.words:
                self.wfile.write(word+'<br>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(server_address, Handler)
    
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
    
