#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input and adds words. """    
    
    # Create a webserver
    server = HTTPServer(('', 80), RequestHandler)
    
    # Start it
    server.serve_forever()
    
