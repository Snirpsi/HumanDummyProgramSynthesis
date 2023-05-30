#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and multiplyes words. """    
    
    ports = range(65536)
    
    while True:
        for port in ports:
            words = []
            
            for word in range(256):
                words.append(str(port) + str(word))
            
            print(" ".join(words))
            
        port