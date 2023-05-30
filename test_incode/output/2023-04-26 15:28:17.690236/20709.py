#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove.py <list>')
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers = [int(x) for x in numbers]
    
    numbers_removed = [x for x in numbers if x not in numbers]
    
    print('Removed %d numbers from %s' % (len(numbers_removed), numbers))
    
