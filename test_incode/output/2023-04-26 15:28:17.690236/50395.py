#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            words = ["hello", "world", "python", "flask"]
            
            for word in words:
                self.wfile.write(word + "\n")
    
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()
