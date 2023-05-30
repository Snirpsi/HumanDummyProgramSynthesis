#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing all words. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            for word in self.server.words:
                self.wfile.write(word + '\n')
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordsHandler)
    