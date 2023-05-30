#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(1, port+1):
        numbers.append(x)
    
    print("Numbers: %s" % numbers)
    
