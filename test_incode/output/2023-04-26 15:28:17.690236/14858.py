#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and iterates over all ports. """    
    
    # Start server
    server = HTTPServer(('', 0), Handler)
    server.serve_forever()
    
