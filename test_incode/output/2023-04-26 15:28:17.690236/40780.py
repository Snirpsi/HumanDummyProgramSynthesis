#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or stores a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordListHandler)
    
    # Start it
    server.serve_forever()
    
