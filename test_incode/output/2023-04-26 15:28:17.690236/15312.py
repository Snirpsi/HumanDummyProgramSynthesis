#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and enumerates words. """    
    
    ports = range(65535)
    words = []
    
    for port in ports:
        words.append(str(port) + "