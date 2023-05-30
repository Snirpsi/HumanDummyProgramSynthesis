#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or enumerates words. """    
    
    words = input('Enter a word: ').split()
    
    for word in words:
        print(word)
    
