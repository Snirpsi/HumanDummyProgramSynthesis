#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input or iterates over a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), MyHandler)
    
    # Start it
    server.serve_forever()
    
