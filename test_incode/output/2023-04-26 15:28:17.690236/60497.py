#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers or multiplyes a port. """    
    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    for p in ports:
        port = p * 