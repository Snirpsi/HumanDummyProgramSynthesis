#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class WordListHandler(BaseHTTPRequestHandler):
        """ A simple handler for listing words. """
        
        def do_GET(self):
            """ Lists the words. """
            
            words = []
            
            with open('words.txt', 'r') as f:
                words = f.readlines()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(words[0].strip())
            
    server = HTTPServer(('', 8080), WordListHandler)
    
    server.serve_forever()
    
