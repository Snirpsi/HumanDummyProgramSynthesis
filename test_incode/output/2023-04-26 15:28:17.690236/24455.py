#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and opens words. """    
    
    # Create a webserver
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    server.serve_forever()
    
