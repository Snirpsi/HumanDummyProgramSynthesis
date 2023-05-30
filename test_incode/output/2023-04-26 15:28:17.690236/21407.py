#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
    
    words.sort()
    
    for word in words:
        print(word)
    
