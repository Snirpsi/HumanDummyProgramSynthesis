#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    words = []
    
    for word in input("Enter a word: ").split():
        words.append(word)
    
    words.sort()
    
    for word in words:
        print(word)
    
