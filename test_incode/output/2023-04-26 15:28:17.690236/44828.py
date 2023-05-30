#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for _ in range(port):
        numbers.append(int(input()))
    
    print('\n'.join(map(str, numbers)))
    
