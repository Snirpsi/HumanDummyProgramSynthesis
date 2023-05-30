#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or removes a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    ports.remove(0)
    ports.remove(1)
    ports.remove(2)
    ports.remove(3)
    ports.remove