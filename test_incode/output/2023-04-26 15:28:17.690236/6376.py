#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    # Create a webserver
    webserver = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    webserver.serve_forever()
