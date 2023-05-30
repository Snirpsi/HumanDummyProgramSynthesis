#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = sys.argv[1:]
    
    numbers = []
    for word in words:
        try:
            numbers.append(int(word))
        except ValueError:
            print('Invalid number: %s' % word)
            sys.exit(1)
    
    print('Numbers:')
    for number in numbers:
        print('  %s' % number)
    
