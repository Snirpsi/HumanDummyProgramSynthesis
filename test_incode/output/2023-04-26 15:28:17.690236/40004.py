#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port or adds words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            port = self.path.rfind('/')
            if port > 0:
                port = self.path[port+1:]
                
            port = int(port)
            
            if port > 0:
                port = ':'+str(port)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(str(port)+'\n')
            
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()
    
