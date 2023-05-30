#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and multiplyes a port. """    
    port = int(sys.argv[1])
    multiplier = 1
    for port in range(port, port+multiplier):
        print(port*multiplier)
