#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of numbers or multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = [x*y for x,y in zip(ports,ports)]
    ports = sum(ports)
    print(ports)
    
