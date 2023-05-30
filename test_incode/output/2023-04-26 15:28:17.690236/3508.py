#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()
