#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = [w for w in open('words.txt')]
    for word in words:
        print(word)
