#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or iterates over a port. """    
    
    # Create a server
    server = HTTPServer(('', PORT), WordsHandler)
    
    # Start it
    server.serve_forever()
    
