#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers. """    
    
    # Create a server
    server = HTTPServer(('', 8080), Number