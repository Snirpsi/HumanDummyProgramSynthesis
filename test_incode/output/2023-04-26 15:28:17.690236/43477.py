#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or opens words. """    
    
    ports = openports()
    words = []
    for port in ports:
        words.append(openword(port))
    
    word