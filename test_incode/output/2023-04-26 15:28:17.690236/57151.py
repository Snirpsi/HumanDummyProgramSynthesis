#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words and removes words. """    
    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    removed = list(filter(lambda x: x not in words, words))
    
    print(removed)
    
