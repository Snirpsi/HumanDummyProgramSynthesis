#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = []
    
    for i in range(1, port+1):
        numbers.append(i)
    
    print(numbers)
    
