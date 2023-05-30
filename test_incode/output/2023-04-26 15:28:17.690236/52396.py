#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and stores a port. """    
    words = []
    port = 1
    while True:
        words.append(input("Enter a word: "))
        port = port + 1
        if port == 