#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and enumerates a port. """    
    
    port = 8080
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
