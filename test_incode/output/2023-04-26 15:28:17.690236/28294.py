#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    # Create a server
    server = HTTPServer(('', 80), RequestHandler)
    
    # Start it
    server.serve_forever()
    
