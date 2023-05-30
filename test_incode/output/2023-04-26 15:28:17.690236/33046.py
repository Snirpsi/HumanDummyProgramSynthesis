#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and iterates over words. """    
    
    ports = openports()
    
    for port in ports:
        words = openword(port)
        
        for word in words:
            print(word)
            
