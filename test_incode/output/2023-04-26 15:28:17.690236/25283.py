#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and calculates a list of words. """    
    
    ports = Ports()
    
    for port in ports.ports:
        words = port.get_words()
        
        for word in words:
            print(word)
            
