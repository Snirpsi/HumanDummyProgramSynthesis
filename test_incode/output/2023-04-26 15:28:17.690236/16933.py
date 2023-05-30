#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or multiplyes a list of words. """    
    
    ports = [int(i) for i in input("Enter a port number: ").split()]
    words = [input("Enter a word: ").split()]
    
    for port in ports:
        for word in words:
            print(port * word)
            
