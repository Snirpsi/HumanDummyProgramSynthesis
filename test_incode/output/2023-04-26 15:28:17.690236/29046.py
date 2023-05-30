#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Define the web server
    server = HTTPServer(('', 8000), Handler)
    
    # Start listening
    server.serve_forever()
    
