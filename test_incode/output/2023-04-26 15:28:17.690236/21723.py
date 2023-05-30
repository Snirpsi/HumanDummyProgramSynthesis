#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and prints numbers. """    
    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = map(int, numbers)
    
    for number in numbers:
        print(number)
        
