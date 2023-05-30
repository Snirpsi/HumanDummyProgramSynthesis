#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = float(number)
        
        if number < 0:
            print('Negative numbers are not allowed')
            sys.exit()
        
        if number == 0:
            print('Zero numbers are not allowed')
            sys.exit()
        
        print('The number %s is equal to %s' % (number, number