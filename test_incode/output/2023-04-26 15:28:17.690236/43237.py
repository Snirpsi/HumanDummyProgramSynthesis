#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input or removes a list of words. """    
    
    # Create a webserver
    server = HTTPServer(('', 8080), RequestHandler)
    
    # Start it
    server.serve_forever()
    
