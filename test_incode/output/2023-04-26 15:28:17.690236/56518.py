#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and stores all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(self.server.words))
    
    server = HTTPServer(('', 8080), WordsHandler)
    server.serve_forever()
    
