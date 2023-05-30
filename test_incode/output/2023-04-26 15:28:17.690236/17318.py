#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 22
    
    numbers = range(port)
    
    for number in numbers:
        print(number)
    
