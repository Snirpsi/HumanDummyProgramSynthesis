#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Create a server
    server = HTTPServer(('', 80), WordRemover)
    
    # Start it
    server.serve_forever()
    
