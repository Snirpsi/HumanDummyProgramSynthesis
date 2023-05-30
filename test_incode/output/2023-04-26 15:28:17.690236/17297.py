#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or enumerates all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import socket
    import random
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request handler. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ GET request to root path. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html>')
                self.wfile.write(b'<head><title>Words Enumeration</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>Words Enumeration</h1>')
                self.wfile.write(b'<p>')
                
                words = []
                
                for port in range(1, 65535):
                    """ Generate random words and print to web page. """
                    words.append(random.choice(string.ascii_uppercase + string.digits))
                    
                    self.wfile.write(b'<p>')
                    self.wfile.write(b'<a href="http://localhost:%s/">%s</a>' % (port, words[-1]))
                    self.wfile.write(b'</p>')
                    
                self.wfile.write(b'</body></html>')
                
            elif parsed_url.path == '/words':
                """ GET request to /words path. """
                
                words = []
                
                for port in range(1, 65535):
                    """ Generate random words and print to web page. """
                    words.append(random.choice(string.ascii_uppercase + string.digits))
                    
                    self.wfile.write(b'<p>')
                    self.wfile.write(b'<a href="http://localhost:%s/">%s</a>' % (port, words[-1]))
                    self.wfile.write(b'</p>')
                    
                self.wfile.write(b'</body></html>')
                
            else:
                """ GET request to unknown path. """
                
                self.send_error(404)
                
    httpd = HTTPServer(("", 0), RequestHandler)
    
    httpd.serve_forever()
    
