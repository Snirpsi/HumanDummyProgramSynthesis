#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or prints a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Port must be between 0 and 65535.")
        sys.exit(1)
    
    print("Enumerating ports 