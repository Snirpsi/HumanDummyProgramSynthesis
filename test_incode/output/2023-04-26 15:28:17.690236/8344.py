#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or iterates over fruits. """    
    
    # Start a server
    server = HTTPServer(('', 80), MyHandler)
    
    # Start a server
    