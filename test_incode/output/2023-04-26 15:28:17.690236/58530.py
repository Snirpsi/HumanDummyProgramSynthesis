#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or opens words. """    
    ports = enumeratePorts()
    for port in ports:
        openWord(port)
        
