#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or stores fruits. """    
    
    # Create a webserver
    server = HTTPServer(('', 80), WordsHandler)
    
    # Start it
    server.serve_forever()
    
