#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports or multiplyes a list of words. """    
    import sys
    words = [x.strip() for x in sys.stdin.read().split()]
    ports = [int(y) for y in sys.stdin.read().split()]
    
    for word in words:
        for port in ports:
            print(port * word)
        
