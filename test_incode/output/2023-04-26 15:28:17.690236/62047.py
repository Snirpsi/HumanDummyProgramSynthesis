#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port and calculates numbers. """    
    import sys
    port = int(sys.argv[1])
    number = (port - 1) * 2 + 1
    print(number)
    
