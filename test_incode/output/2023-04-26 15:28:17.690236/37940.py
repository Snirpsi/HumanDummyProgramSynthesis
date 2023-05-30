#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and calculates a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    for i in range(port):
        numbers.append(i)
    print('\n'.join(numbers))
