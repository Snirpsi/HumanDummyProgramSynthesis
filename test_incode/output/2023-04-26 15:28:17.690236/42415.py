#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordHandler(BaseHTTPRequestHandler):
        """ A simple handler for words. """
        
        def do_GET(self):
            """ Respond to a GET request. """
            
            word = self.path.split('/')[-1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes(f'<h1>{word}</h1>', 'utf-8'))
            
    httpd = HTTPServer(("", 8000), WordHandler)
    httpd.serve_forever()
    
