#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and iterates over words. """    
    
    ports = range(1,65535)
    
    words = []
    
    for port in ports:
        words.append(str(port))
        
    for word in words:
        print(word)
        
