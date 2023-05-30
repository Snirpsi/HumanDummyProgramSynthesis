#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or multiplyes numbers. """    
    port = int(sys.argv[1])
    numbers = map(int, sys.argv[2:])
    numbers = map(lambda n: n * port, numbers)
    print(numbers)

<|/ file filename=