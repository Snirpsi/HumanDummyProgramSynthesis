#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or iterates over a port. """    
    port = int(sys.argv[1])
    
    # Create a server
    server = HTTPServer(('', port), Handler)
    
    # Start it
    server.serve_forever()
    
