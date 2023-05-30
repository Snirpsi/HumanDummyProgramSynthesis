#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or iterates over a list of words. """    
    
    # Create a server and listen for requests
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start it
    server.serve_forever()
