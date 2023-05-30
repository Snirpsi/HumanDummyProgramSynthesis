#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and prints words. """    
    words = []
    
    for word in open('words.txt'):
        words.append(word.strip())
    
    for word in words:
        print(word)
    
