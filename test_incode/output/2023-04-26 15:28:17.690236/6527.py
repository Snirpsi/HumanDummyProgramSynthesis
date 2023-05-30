#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(
                "Hello, world! This is a simple web server that adds words.")
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordHandler)
    
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
    
