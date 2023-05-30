#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and returns a port. """    
    port = int(sys.argv[1])
    
    # Start a server
    server = HTTPServer(('', port), Handler)
    
    # Start a client
    