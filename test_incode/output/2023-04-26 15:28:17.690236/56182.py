#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python addnums.py <numlist>')
        sys.exit()
    
    numlist = sys.argv[1:]
    
    for num in numlist:
        print(num