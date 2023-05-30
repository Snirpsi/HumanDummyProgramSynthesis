#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(1, port+1):
        numbers.append(x)
        
    numbers_str = ','.join(map(str, numbers))
    
    print('Content-type: text/plain')
    print('')
    print('The numbers 1 to {} are {}.'.format(port, numbers_str))
    print('')
    
