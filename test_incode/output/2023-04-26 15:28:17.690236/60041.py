#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and iterates over a port. """    
    
    port = 8080
    
    server = HTTPServer(('', port), Handler)
    server.serve_forever()
    
