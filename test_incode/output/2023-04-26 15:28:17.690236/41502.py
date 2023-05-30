#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    # Create a simple server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    server.serve_forever()
    
