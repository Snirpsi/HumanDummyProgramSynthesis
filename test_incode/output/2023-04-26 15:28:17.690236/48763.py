#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns all ports and enumerates words. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        words = enumerate_words(port)
        
        for word in words:
            print(word, port)
    
