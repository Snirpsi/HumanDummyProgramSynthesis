#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                """ Return index.html. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Words</h1>')
                self.wfile.write(b'</body></html>')
                return
            
            if path == '/words':
                """ Return words.txt. """
                
                from words import Words
                
                words = [Word(word) for word in Words()]
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'\n'.join(words))
                return
            
            if path == '/words/<word>':
                """ Return word.txt. """
                
                from words import Word
                
                word = Word(self.path.split('/')[1])
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(word.word