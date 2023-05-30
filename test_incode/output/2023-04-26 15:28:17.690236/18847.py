#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits or iterates over a port. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s [port]" % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    print("Printing fruits...")
    
    fruits = Fruits(port)
    
    for fruit in fruits:
        print(