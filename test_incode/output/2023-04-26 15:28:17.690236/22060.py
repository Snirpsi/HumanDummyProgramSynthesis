#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and returns a port. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    for i in range(1, port+1):
        numbers.append(i)
    
    numbers_str = ','.join(numbers)
    
    