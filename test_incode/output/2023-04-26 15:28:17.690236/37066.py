#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        multiplied = []
        for word in words:
            multiplied.append(word*