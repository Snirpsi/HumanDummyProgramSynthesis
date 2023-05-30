#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and calculates a list of words. """    
    
    ports = range(1,51)
    
    words = []
    for port in ports:
        words.append(str(port)+'