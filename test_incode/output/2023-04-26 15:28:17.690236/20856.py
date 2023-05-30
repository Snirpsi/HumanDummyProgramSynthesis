#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and enumerates a list of words. """    
    ports = enumerate_ports()
    words = enumerate_words()
    
    for port in ports:
        for word in words:
            print(port + ' ' + word)
        
