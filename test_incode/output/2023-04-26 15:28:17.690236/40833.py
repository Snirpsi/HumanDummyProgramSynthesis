#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python add_numbers.py <list>")
        sys.exit()
    
    numbers = map(int, sys.argv[1].split(','))
    
    print(*numbers, sep=',')
    
