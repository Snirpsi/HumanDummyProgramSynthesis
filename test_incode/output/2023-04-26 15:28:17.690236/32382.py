#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and iterates over all ports. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(("", port), WordsHandler)
    
    # Start it
    server.serve_forever()
    
