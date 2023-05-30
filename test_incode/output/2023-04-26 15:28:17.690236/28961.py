#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or converts all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python list.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        print(port)
    
