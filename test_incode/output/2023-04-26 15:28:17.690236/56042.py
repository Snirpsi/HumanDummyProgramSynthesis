#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and opens numbers. """    
    port = int(sys.argv[1])
    
    numbers = range(port)
    
    for number in numbers:
        number = str(number)
        
        open