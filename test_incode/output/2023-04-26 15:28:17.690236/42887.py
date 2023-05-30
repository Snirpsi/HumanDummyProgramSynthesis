#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and calculates fruits. """    
    
    # Create a webserver
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()
    
