#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or stores numbers. """    
    
    # Create a webserver
    server = HTTPServer(('', 8000), WordServer)
    
    # Start it
    server.serve_forever()
    
