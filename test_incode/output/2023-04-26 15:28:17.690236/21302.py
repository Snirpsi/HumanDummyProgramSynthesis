#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import random
    
    server_address = ('localhost', 8000)
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the contents of the 
            requested file. """
            path = urlparse(self.path).path
            
            if path == '/':
                """ Respond with a 404 error code """
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(bytes('<html><head><title>404</title></head>'
                                        '<body>404</body></html>', 'utf8'))
                sys.exit(0)
            
            """ Respond with a 403 error code """
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><head><title>403</title></head>'
                                    '<body>403</body></html>', 'utf8'))
            sys.exit(0)
            
            """ Respond with a 200 OK status code """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            """ Generate a random list of words and send it back. """
            words = []
            
            for i in range(10):
                """ Generate a random word and add it to the list. """
                word = random.choice(['cat', 'dog', 'bird', 'fish', 'cat', 'dog', 'bird', 'fish'])
                words.append(word)
                
            """ Send the list of words to the client. """
            self.wfile.write(bytes(
                '<html><head><title>Words</title></head>'
                '<body>%s</body></html>' % '\n'.join(words),
                'utf8'))
            sys.exit(0)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting Words Server on port 8000')
    httpd.serve_forever()
    
