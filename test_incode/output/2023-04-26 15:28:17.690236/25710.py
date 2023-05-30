#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and multiplyes all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    ports = ports * len(ports)
    print(ports)
    
