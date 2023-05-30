#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words. """    
    words = open('words.txt').read().splitlines()
    
    words.sort()
    
    for word in words:
        print(word)
        
