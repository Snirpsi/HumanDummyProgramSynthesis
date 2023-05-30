#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports = [p*2 for p in ports]
    print(ports)
    
