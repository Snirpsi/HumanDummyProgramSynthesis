#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and adds a list of words. """    
    
    ports = range(10000, 20000)
    words = []
    
    for port in ports:
        words.append(str(port))
        
    print('\n'.join(words))
    
