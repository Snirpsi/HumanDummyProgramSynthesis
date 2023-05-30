#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port or returns a port. """    
    
    port = None
    try:
        port = int(sys.argv[1])
    except:
        print("Usage: python ports.py <port>")
        sys.exit(1)
    
    ports.store(port)
    
