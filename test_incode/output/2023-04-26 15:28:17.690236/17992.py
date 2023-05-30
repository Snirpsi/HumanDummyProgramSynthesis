#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port or converts a list of words. """    
    while True:
        line = input()
        words = line.split(' ')
        
        port = int(words[0])
        
        if port == -1:
            port = 0
        
        words[0] = words[0]