#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    words = []
    
    words.append(input("Enter a word: "))
    
    words = words + list(set(words))
    
    words.sort()
    
    print(" ".join(words))
    
