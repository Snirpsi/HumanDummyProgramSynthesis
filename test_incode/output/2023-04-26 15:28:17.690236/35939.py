#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers and enumerates a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()

