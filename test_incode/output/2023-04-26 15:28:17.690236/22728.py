#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers. """    
    
    numbers = sys.argv[1:]
    
    numbers = [int(x) for x in numbers]
    
    numbers = numbers[: