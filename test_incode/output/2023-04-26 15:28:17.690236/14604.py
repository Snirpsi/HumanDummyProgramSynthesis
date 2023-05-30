#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and adds a port. """    
    
    port = 8080
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
    
