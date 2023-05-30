#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordHandler(BaseHTTPRequestHandler):
        """ Handle requests for words. """
        
        def do_GET(self):
            """ Handle requests for words. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                path = 'index.html'
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open(path) as file:
                self.wfile.write(file.read())
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordHandler)
    
    print('Starting httpserver on port 8080')
    httpd.serve_forever()
    
