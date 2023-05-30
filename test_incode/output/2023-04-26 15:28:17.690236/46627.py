#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers and stores a list of words. """    
    words = []
    while True:
        words.append(input())
        if len(words) == 