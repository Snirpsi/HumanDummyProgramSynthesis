#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or opens all ports. """    
    
    import sys
    
    if len(sys.argv) == 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[1:]
    
    ports = []
    
    for word in words:
        ports.append(open(word, 'rb'))
    
    for port in ports:
        port.close()
    
    for port in ports:
        port.