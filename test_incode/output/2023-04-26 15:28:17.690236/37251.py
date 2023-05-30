#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from multiprocessing import Process
    
    HOST, PORT = 'localhost', 8080
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that multiplies a list of words. """
        
        def do_GET(self):
            """ Handle a GET request to /. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Hello World!</h1>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
                
    httpd = HTTPServer((HOST, PORT), RequestHandler)
    
    print('Serving on http://%s:%s/' % (HOST, PORT))
    httpd.serve_forever()
    
