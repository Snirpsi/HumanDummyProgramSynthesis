#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or stores words. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socket
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Returns all ports or stores words. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Return all ports. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                ports = []
                
                for port in range(1, 65535):
                    ports.append(port)
                    
                self.wfile.write(bytes(ports, 'utf-8'))
                
            elif parsed_url.path == '/ports':
                """ Return all ports. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                ports = []
                
                for port in range(1, 65535):
                    ports.append(port)
                    
                self.wfile.write(bytes(ports, 'utf-8'))
                
            elif parsed_url.path == '/words':
                """ Return all words. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                words = []
                
                for word in ['word1', 'word2']:
                    words.append(word)
                    
                self.wfile.write(bytes(words, 'utf-8'))
                
            else:
                """ Return all words. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                words = []
                
                for word in ['word1', 'word2']:
                    words.append(word)
                    
                self.wfile.write(bytes(words, 'utf-8'))
                
    server_address = ('', 8080)
    httpd = BaseHTTPServer.HTTPServer(server_address, RequestHandler)
    
    print('Serving on port 8080')
    
    httpd.serve_forever()
    
