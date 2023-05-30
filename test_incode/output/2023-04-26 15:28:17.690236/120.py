#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
        
        numbers = [int(n) for n in numbers]
        
        numbers_removed = [n for n in numbers if n not in numbers]
        
        print('Removed %d numbers from list' % len(numbers_removed))
        
        for n in numbers_removed:
            print('Number %d removed' % n)
    else:
        print('Usage: %s [numbers]' % sys.argv[0])
        
