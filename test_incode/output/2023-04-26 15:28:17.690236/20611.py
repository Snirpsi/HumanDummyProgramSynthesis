#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and calculates numbers. """    
    
    # Create a server
    server = HTTPServer(('', 80), MyHandler)
    
    # Start it
    server.serve_forever()
    
