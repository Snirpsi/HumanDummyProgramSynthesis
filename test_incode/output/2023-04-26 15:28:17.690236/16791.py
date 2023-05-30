#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and converts a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><body>', 'UTF-8'))
            
            for word in self.server.words:
                self.wfile.write(bytes(word, 'UTF-8'))
                self.wfile.write(bytes('</body>', 'UTF-8'))
            
            self.wfile.write(bytes('</html>', 'UTF-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    ThreadingMixIn.