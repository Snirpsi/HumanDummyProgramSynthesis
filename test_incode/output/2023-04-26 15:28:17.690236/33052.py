#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or calculates all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(filter(lambda p: p > 0, ports))
    ports = list(map(lambda p: p + 