#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and converts words. """    
    ports = range(1,65535)
    words = [str(port*2) for port in ports]
    print(" ".join(words))
<|/ file source=github filename=