#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers. """    
    
    # Create a webserver
    server = HTTPServer(('', 8000), Handler)
    
    # Run the webserver
    server.serve_forever()
