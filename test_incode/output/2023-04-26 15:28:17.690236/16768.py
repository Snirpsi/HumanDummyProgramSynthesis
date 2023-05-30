#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and stores all ports. """    
    ports = []
    
    # Start a server that listens on all available ports
    server = HTTPServer(('', 0), MyHandler)
    
    # Start a server that listens on port 80
    server_80 = HTTPServer(('', 80), MyHandler)
    
    # Start a server that listens on port 8080
    server_808