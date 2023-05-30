#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or converts a port. """    
    
    port = 8080
    
    # Start a server
    server = HTTPServer(('', port), MyHandler)
    
    # Start a client
    