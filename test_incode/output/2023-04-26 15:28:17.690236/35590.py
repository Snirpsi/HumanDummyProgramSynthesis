#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordListHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request with a list of words. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            words = []
            
            for word in self.path.split('/'):
                words.append(word.title())
            
            self.wfile.write(