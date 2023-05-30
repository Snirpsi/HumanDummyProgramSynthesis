#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words and iterates over words. """    
    
    # Create a web server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()
    
