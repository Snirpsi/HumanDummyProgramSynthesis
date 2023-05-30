#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <numbers>' % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number < 0:
            print('Error: %s cannot be negative' % number)
            sys.exit()
        
        if number == 0:
            print('Error: %s cannot be zero' % number)
            sys.exit()
        
        number = str(number)
        
        print('%s is %s' % (number, number