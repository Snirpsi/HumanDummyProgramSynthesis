#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports and adds a list of words. """    
    ports = []
    
    while True:
        ports.append(getPort())
        
        for word in words:
            print(word, end='