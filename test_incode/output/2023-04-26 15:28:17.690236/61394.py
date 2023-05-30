#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    with open('numbers.txt', 'r') as numbers_file:
        for line in numbers_file:
            numbers.append(int(line))
    
    numbers = list(set(numbers))
    
    numbers_