#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or iterates over numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit(1)
    
    numbers = sys.argv[1].split(',')
    
    for number in numbers:
        number = int(number)
        
        if number < 1:
            print('Negative numbers are not allowed')
            sys.exit(1)
        
        if number % 2 == 0:
            print('%d is even' % number)
        else:
            print('%d is odd' % number)
