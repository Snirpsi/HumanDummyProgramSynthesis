#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or removes fruits. """    
    
    words = input("Enter words: ")
    fruits = input("Enter fruits: ")
    
    words = words.split()
    fruits = fruits.split()
    
    words = filter(None, words)
    fruits = filter