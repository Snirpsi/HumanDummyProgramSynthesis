#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words or stores all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3']
    
    for port in ports:
        