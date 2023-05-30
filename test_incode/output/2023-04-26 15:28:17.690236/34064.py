#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    multiplier = 1
    
    if port > 0:
        multiplier = 1
        
    for x in range(port):
        multiplier = multiplier * x
    
    print(multiplier)
    
