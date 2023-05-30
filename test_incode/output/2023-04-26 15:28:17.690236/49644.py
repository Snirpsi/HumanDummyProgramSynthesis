#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <number>' % sys.argv[0])
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print('Usage: %s <number>' % sys.argv[0])
        sys.exit(1)
    
    print('%i -> %i' % (number, number * 2))
    
