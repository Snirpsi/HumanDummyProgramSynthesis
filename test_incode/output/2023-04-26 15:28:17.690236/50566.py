#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    else:
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    numbers = list(map(int, numbers))
    
    numbers_removed = list(filter(lambda number: number not in numbers, numbers))
    
    print(numbers_removed)
    
