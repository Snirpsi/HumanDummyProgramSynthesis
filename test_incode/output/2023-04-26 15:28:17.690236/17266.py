#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input. """    
    
    # Start a webserver on port 8000.
    server = HTTPServer(('', 8000), Handler)
    
    # Wait forever for incoming requests.
    server.serve_forever()
