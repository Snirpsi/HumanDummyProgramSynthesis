#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words or iterates over fruits. """    
    
    # Create a server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start it
    server.serve_forever()
    
