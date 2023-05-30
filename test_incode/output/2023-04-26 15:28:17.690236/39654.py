#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and prints numbers. """    
    port = int(sys.argv[1])
    
    multiplier = 1
    
    for digit in range(10):
        multiplier = multiplier * 10
        
    print(port * multiplier)
    
