#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and calculates fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python numbers.py')
        exit(1)
    
    numbers = sys.argv[1:]
    
    for number in numbers:
        number = int(number)
        
        if number > 0:
            print('{} * {} = {}'.format(number, number * 2, number * 