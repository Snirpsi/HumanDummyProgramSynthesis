#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or returns words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s [numbers]' % sys.argv[0])
        print('numbers: a list of numbers')
        
    elif len(sys.argv) == 2:
        numbers = sys.argv[1:]
        
        for number in numbers:
            print(number)
            
    else:
        print('Usage: %s [numbers]' % sys.argv[0])
        print('numbers: a list of numbers')
        
