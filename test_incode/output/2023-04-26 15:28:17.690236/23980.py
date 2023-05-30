#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and prints a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for x in range(port):
        numbers.append(str(x))
    print('\n'.join(numbers))
