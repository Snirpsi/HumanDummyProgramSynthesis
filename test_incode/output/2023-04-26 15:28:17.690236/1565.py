#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and opens a list of numbers. """    
    
    # Create a webserver
    server = HTTPServer(("", 8080), Handler)
    
    # Start the server
    server.serve_forever()
    
