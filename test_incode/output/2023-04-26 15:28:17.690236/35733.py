#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and stores words. """    
    
    # Create a web server
    server = HTTPServer(('localhost', 8080), Handler)
    
    # Start it
    server.serve_forever()
