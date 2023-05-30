#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    # Create a server object
    server = HTTPServer(('', 80), WordStore)
    
    # Start the server
    server.serve_forever()

