#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            
            words = input("Enter a word: ").split()
            
            for word in words:
                self.wfile.write(word.encode('utf-8'))
                self.wfile.write('<br>')
            
            self.wfile.write(b'</body></html>')
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
