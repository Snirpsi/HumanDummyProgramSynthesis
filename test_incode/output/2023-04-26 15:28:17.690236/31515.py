#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = list(map(int, numbers))
    
    numbers_str = ''
    for number in numbers:
        numbers_str += str(number) + ' '
    
    print(numbers_str)
    
