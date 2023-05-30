#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and calculates numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.sort()
    
    numbers = []
    for port in ports:
        numbers.append(port * 2)
    
    print(numbers)
    
