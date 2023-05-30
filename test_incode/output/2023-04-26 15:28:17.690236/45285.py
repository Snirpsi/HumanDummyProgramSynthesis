#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and calculates a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 80), WordsHandler)
    
    # Start it
    server.serve_forever()
