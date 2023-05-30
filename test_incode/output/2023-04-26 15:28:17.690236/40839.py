#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and calculates all ports. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ports = []
    for word in words:
        ports.append(len(word))
    print(ports)
    
