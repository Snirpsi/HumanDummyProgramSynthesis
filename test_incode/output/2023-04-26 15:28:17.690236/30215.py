#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or prints fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    if port < 0 or port > 65535:
        print("Port must be between 0 and 65535")
        exit(1)
    
    fruits = convert_port(port)
    
    for fruit in fruits:
        print(