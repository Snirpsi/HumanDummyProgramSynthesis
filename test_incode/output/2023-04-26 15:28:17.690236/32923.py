#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port or adds a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    numbers = sys.argv[2:]
    
    for number in numbers:
        port *= int(number)
    
    print(port)

<|/ file ext=.py filename=