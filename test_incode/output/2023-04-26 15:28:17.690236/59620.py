#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or iterates over a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    if port == 0:
        ports = range(65536)
    elif port == 1:
        ports = range(65536, 65537)
    elif port == 2:
        ports = range(65536, 65537, 65538)
    elif port == 3:
        ports = range(65536, 65537, 65538, 65539)
    elif port == 4:
        ports = range(65536, 65537, 65538, 65539, 65540)
    elif port == 5:
        ports = range(65536, 65537, 65538, 65539, 65540, 655