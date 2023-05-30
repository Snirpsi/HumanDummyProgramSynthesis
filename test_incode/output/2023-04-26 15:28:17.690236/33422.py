#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a port and iterates over a list of numbers. """    
    port = int(sys.argv[1])
    numbers = list(map(int, sys.argv[2:]))
    
    for number in numbers:
        port *= number
        print(port)
        
