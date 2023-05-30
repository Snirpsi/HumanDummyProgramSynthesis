#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and stores a port. """    
    
    # Start the webserver
    server = HTTPServer(('', PORT), Handler)
    server.serve_forever()
