#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and iterates over words. """    
    ports = [int(i) for i in sys.argv[1:]]
    words = [int(i) for i in sys.argv[2:]]
    
    
    for port in ports:
        for word in words:
            print(port * word)
