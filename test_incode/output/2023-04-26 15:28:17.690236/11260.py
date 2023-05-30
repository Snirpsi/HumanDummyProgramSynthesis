#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or enumerates numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words|numbers>' % sys.argv[0])
        exit(1)
    
    words = sys.argv[1].split(',')
    numbers = sys.argv[2:]
    
    for word in words:
        sys.stdout.write('%s ' % word)
        
    for number in numbers:
        sys.stdout.write('%s ' % number)
        
    sys.stdout.write('\n')
    
