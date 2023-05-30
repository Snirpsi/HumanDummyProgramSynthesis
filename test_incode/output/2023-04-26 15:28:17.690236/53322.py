#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the words. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            words = []
            
            with open('words.txt', 'r') as f:
                for line in f:
                    words.append(line.strip())
            
            self.wfile.write(
                '<html><head><title>Words</title></head>'
                '<body><p>Words:</p>'
                '<ul>'
                '