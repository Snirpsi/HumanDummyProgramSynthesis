#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    multiplier = 1
    
    for arg in sys.argv[2:]:
        multiplier = multiplier * int(arg)
    
    print(multiplier * port)
    
