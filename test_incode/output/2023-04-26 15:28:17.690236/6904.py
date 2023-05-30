#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port or enumerates a list of numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    for port in ports:
        print(port)

<|/ file ext=.py source=github |>