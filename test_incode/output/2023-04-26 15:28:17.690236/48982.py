#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints numbers and adds a port. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = range(port)
    
    for number in numbers:
        print(number)
        
