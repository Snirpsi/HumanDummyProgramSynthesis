#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port. """    
    import sys
    port = int(sys.argv[1])
    
    ports = []
    
    for port in range(port, 65535):
        ports.append(port)
    
    for port in ports:
        print("Port {} is open.".format(port))
    
