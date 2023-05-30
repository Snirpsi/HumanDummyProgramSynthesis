#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or opens a port. """    
    port = int(sys.argv[1])
    
    if port == 80:
        openPort()
    elif port == 443:
        openPort(443)
    else:
        openPort(port)
    
