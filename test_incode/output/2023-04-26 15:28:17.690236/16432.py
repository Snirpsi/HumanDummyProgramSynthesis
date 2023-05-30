#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    numbers = [n * port for n in numbers]
    
    print('\n'.join(map(str, numbers)))
    
