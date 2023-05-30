#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordsHandler(BaseHTTPRequestHandler):
        """ A simple handler for words. """
        
        def do_GET(self):
            """ Respond to GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(
                "\n".join(self.server.words).encode('utf-8')
                )
            
    httpd = HTTPServer(("", 80), WordsHandler)
    
    print("Serving on port 80")
    httpd.serve_forever()
    
