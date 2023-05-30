#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    # Start a webserver
    server = HTTPServer(("", 80), Words