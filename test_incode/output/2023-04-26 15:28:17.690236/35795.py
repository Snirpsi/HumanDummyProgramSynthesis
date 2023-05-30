#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and calculates a list of words. """    
    
    ports = range(1,10)
    words = []
    
    for port in ports:
        words.append(str(port*2))
    
    print(" ".join(words))
    
