#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port and adds fruits. """    
    
    port = open("/dev/ttyUSB0","w")
    port.write("Fruit 