#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or opens a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [i for i in range(port, 65535)]
    
    ports.reverse()
    
    for port in ports:
        print("Port {}