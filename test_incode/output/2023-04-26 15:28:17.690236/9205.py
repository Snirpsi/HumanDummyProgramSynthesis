#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or returns a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from sys import argv
    
    port = 8080
    
    if len(argv) > 1:
        port = int(argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
class MyHandler(BaseHTTPRequestHandler):
    """ A simple HTTP request handler that prints the contents of a file """
    def do_GET(self):
        """ Handle a GET request """
        
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server.wordlist)
            self.wfile.close()
        else:
            self.send_error(404)
    
    def log_message(self, format, *args):
        """ Log messages """
        return
    
