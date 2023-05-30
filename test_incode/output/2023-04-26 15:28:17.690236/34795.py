#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and calculates a port. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    port = 0
    for word in words:
        port += ord(word) - ord('a