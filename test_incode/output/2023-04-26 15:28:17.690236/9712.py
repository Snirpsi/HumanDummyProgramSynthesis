#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or adds a port. """    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = range(1,65535)
    
    for port in ports:
        print("Port", port, "=", port*2)
    
