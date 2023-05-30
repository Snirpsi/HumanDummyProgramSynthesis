#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and returns numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    for port in ports:
        print(port)

<|/ file filename=ports.py |>