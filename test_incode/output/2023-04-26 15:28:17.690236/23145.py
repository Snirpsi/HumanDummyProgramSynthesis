#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers or converts a list of words. """    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: python enumerate.py <list>')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        print(number)
    
