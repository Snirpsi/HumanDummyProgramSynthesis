#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and calculates a list of numbers. """    
    
    # Create a server
    server = HTTPServer(('', 80), WordServer)
    
    # Start it
    server.serve_forever()
    
