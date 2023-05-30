#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    # Create a simple HTTP server
    server = HTTPServer(("", 80), WordsHandler)
    
    # Start it
    server.serve_forever()

<|/ file source=github filename=word