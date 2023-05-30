#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordHandler(BaseHTTPRequestHandler):
        """ A handler for words. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            word = self.path.split('/')[1]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(word.encode('utf-8'))
    
    httpd = HTTPServer(("", 8000), WordHandler)
    
    print("Serving at port 8000...")
    
    httpd.serve_forever()
    
