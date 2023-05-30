#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    for word in input().split():
        words.append(word)
    
    print(" ".join(words))
    
