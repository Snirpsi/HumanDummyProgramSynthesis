#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and stores a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(1, port+1):
        numbers.append(i)
    
    