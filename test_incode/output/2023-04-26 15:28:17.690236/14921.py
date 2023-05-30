#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and prints a list of numbers. """    
    port = int(sys.argv[1])
    numbers = range(port)
    print(numbers)
