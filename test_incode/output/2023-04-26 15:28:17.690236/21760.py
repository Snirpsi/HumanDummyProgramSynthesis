#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and returns a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    
    while port > 0:
        numbers.append(port % 10)
        port /= 10
    
    print(numbers)
    
