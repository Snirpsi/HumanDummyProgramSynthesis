#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and returns a port. """    
    
    port = int(sys.argv[1])
    
    numbers = range(port)
    
    ports = []
    for number in numbers:
        ports.append(number)
    
    print('\n'.join(map(str, ports)))
    
