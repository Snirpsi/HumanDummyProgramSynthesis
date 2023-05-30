#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    words = open("words.txt", "r").read().splitlines()
    for word in words:
        