#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and multiplyes a list of numbers. """    
    ports = [int(i) for i in sys.argv[1].split(',')]
    ports = [x*y for x,y in zip(ports, ports)]
    print(ports)
