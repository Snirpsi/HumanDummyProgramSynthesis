#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and calculates a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(0, port):
        numbers.append(i)
    
    