#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        print('Example: %s 100' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number < 0:
            print('Negative numbers are not allowed')
            sys.exit()
        
        if number > sys.maxsize:
            print('Number too large')
            sys.exit()
        
        print('%d is %d' % (number, number))
    
