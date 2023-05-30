#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and iterates over a port. """    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), WordsHandler)
    
    # Start it
    server.serve_forever()
    
