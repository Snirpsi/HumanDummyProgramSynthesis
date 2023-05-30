#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    multiplier = 1
    
    for x in range(1, port+1):
        multiplier = multiplier * x
    
    print(multiplier)
    
