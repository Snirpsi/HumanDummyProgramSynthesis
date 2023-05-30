#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or multiplyes a list of words. """    
    import sys
    import socketserver
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import random
    
    HOST = 'localhost'
    PORT = 8000
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            query = parse_qs(urlparse(self.path).query)
            
            if query['q'] == 'quit':
                self.send_response(200)
                self.end_headers()
                return
            
            if query['q'] == 'multiply':
                words = []
                
                for word in query['words']:
                    words.append(word)
                
                words.sort()
                
                self.send_response(200)
                self.end_headers()
                
                self.wfile.write(b'\n'.join(words))
                return
            
            self.send_response(200)
            self.end_headers()
            
            self.wfile.write(b'')
            
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    
    print('Serving on port 8000')
    httpd.serve_forever()
    
