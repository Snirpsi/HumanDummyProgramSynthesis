#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    with open('numbers.txt') as f:
        for line in f:
            numbers.append(int(line))
    
    numbers = sorted(numbers)
    
    