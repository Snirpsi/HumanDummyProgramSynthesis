#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and opens a port. """    
    
    port = int(sys.argv[1])
    
    words = [
        "Hello",
        "World",
        "!