#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = glob.glob('/dev/ttyUSB*')
    for port in ports:
        