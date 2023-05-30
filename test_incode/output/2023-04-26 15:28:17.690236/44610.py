#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = list(filter(lambda x: x != '', numbers))
    
    for number in numbers:
        print(number)
    
