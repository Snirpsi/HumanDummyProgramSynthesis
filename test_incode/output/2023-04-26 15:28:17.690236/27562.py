#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and adds words. """    
    ports = sys.argv[1:]
    for port in ports:
        port = int(port)
        ports[port] = ports[port] + ' 