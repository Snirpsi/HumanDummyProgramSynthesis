#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        """ A handler that iterates over a port and prints its content. """
        def do_GET(self):
            """ Handle a GET request. """
            port = self.server.port
            
            for n in range(port):
                self.wfile.write(str(n) + '\n')
            
            self.wfile.write('\nDone\n')
            
    server = HTTPServer(('', int(sys.argv[1])), Handler)
    server.serve_forever()
