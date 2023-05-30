#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or multiplyes a list of words. """    
    ports = sys.argv[1:]
    words = []
    for port in ports:
        words = words + port.split()
    words = list(set(words))
    words.sort()
    for word in words:
        print(word)
    
