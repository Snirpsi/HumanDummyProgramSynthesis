#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and stores a port. """    
    
    port = 8000
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    server.serve_forever()
