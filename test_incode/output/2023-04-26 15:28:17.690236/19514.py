#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), WordStore)
    
    # Start it
    server.serve_forever()
    
