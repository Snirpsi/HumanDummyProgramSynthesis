#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports and multiplyes a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ports = [0] * len(words)
    for index, word in enumerate(words):
        ports[index] = word