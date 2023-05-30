#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = 1
    
    numbers = [str(n) for n in range(number)]
    
    print('\n'.join(numbers))
    
