#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and enumerates a list of words. """    
    
    ports = range(5000, 5999)
    words = []
    
    for port in ports:
        words.append('Port %d' % port)
    
    