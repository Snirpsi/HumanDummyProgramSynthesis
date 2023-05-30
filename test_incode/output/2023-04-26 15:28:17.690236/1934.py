#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and stores a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 80), MyHandler)
    
    # Start it
    server.serve_forever()
    
