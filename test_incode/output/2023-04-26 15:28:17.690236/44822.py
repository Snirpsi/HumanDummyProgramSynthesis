#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports and returns words. """    
    import sys
    ports = sys.argv[1:]
    words = []
    for port in ports:
        words.append(port)
    
    for word in words:
        print(word)
    
