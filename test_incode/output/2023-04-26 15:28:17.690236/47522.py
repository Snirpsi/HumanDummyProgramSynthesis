#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    # Create a web server
    server = HTTPServer(('', 8080), Handler)
    
    # Start the server
    server.serve_forever()
    
