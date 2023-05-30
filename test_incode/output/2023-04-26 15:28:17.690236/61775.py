#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(map(lambda x: x * 2, ports))
    ports.sort()
    ports = ports[: