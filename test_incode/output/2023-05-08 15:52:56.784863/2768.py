#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of words.
    #It will also print out the words in the list.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from sys import argv
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            words = parsed_url.path.split("/")
            
            words = [words[0]] + words[1:]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(words)
    
    server = HTTPServer(('', 8080), Handler)
    ThreadingMixIn.instance().start()
    
    server.serve_forever()

