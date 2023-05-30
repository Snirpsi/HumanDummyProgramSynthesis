#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that prints out the contents of a
        file on disk. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            with open('words.txt', 'r') as f:
                contents = f.read()
                self.wfile.write(contents)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    