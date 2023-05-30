#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words. """    
    
    words = open('words.txt').read().split()
    
    for word in words:
        print(word)
        
