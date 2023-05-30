#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or converts fruits. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 22
    
    fruits = enumeratePorts(port)
    
    for fruit in fruits:
        print('{0}: {1}'.format(fruit[0], fruit[1]))
    
