#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or prints fruits. """    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM1', 'COM2', 'COM3']
        
    for port in ports:
        try:
            