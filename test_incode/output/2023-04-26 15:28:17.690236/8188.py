#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports or prints numbers. """    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        print(port * 