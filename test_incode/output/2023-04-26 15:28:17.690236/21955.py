#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and enumerates a list of numbers. """    
    port = 3000
    numbers = []
    
    while True:
        numbers.append(port * 2)
        port += 1
        
        print('