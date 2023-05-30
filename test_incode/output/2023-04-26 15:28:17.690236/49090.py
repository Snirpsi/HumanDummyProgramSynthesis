#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that enumerates words. """
        
        def do_GET(self):
            """ Respond to a GET request by printing out all words. """
            
            words = []
            
            for word in self.server.words:
                words.append(word)
                
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'\n'.join(words).encode('utf-8'))
    
    server = HTTPServer(('', 8080), RequestHandler)
    
    thread = ThreadingMixIn(