#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socket
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request to /words/ """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/words':
                words = []
                
                words = words + self.server.words
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                self.wfile.write(bytes(words, 'utf8'))
            else:
                self.send_error(404)
    
    server_address = ('localhost', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting webserver on port 8000')
    
    httpd.serve_forever()
    
