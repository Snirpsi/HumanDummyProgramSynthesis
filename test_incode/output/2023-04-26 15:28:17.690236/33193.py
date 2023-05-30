#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or multiplyes words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port < 0 or port > 65535:
            print("Invalid port")
            sys.exit(1)
    
        if port == 65535:
            print("No port specified")
            sys.exit(1)
    
        words = sys.argv[2:]
    
        for word in words:
            print(word*port)
    else:
        print("Usage: python ports.py <port>")
