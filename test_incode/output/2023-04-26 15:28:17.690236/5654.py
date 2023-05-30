#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and multiplyes words. """    
    
    ports = range(65536)
    words = []
    
    for port in ports:
        words.append(str(port*2))
        
    print(" ".join(words))
    
