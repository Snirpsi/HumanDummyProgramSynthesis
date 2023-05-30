#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port and prints a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(port):
        numbers.append(i)
    print('\n'.join(map(str, numbers)))
