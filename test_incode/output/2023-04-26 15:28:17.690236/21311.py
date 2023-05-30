#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and removes words. """    
    port = '/dev/ttyUSB0'
    words = port.split()
    words = [w for w in words if w != '']
    print(" ".join(words))
    
