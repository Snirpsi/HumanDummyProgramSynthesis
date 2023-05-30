#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    numbers = [n * p for n, p in zip(numbers, port)]
    
    print('\n'.join(map(str, numbers)))
    
