#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and returns a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the list of words. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            words = []
            
            for port in range(1, 65535):
                words.append('Port {}'.format(port))
            
            self.wfile.write(b'\n'.join(words))
            
    httpd = HTTPServer(("", 0), Handler)
    
    print("Serving on port {}".format(httpd.server_port))
    
    httpd.serve_forever()
