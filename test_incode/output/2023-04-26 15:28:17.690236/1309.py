#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and calculates a list of numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    numbers = []
    for port in ports:
        numbers.append(port * 2)
    print('\n'.join(map(str, numbers)))
    
