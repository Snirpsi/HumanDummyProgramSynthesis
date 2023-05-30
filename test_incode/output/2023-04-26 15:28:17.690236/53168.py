#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or calculates words. """    
    
    ports = enumerate_ports()
    
    words = []
    for port in ports:
        words.append(ports[port])
    
    print('\n'.join(words))
    
