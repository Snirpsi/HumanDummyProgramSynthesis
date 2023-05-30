#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes all ports or multiplyes a port. """    
    ports = sys.argv[1:]
    for port in ports:
        if port == '--port':
            ports.remove(port)
        elif port == '--ports':
            ports = ports * 2
        else:
            port = int(port)
            port