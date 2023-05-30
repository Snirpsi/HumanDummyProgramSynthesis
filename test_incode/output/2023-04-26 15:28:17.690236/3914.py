#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and stores a list of numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = []
    
    # Start a server
    server = HTTPServer(("", port), NumberServer)
    
    # Start a client
    