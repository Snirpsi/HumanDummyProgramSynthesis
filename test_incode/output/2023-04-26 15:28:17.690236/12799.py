#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM1', 'COM2', 'COM3']
    
    for port in ports:
        print(port)
    
