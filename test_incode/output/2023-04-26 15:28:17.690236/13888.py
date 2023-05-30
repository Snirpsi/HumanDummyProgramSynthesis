#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and multiplyes a port. """    
    
    # Create a webserver
    server = HTTPServer(("", 8080), WordsServer)
    
    # Start it
    server.serve_forever()
    
