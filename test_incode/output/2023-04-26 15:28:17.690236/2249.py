#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or adds a list of words. """    
    words = ["word1", "word2", "word3"]
    
    while True:
        words = words + ["word4"]
        
        print(words)
        
