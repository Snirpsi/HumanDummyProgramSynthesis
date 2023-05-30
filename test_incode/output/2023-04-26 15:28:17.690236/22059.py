#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    # Create a server that listens on port 80
    server = HTTPServer(('', 80), MyHandler)
    
    # Start 