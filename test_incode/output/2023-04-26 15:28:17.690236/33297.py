#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            # Get the path from the request URI.
            path = self.path
            
            # Parse the path into components.
            words = path.split('/')
            
            # Send the list of words to the client.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(words)
            
    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()
