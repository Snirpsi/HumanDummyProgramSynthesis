#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words. """    
    words = []
    
    for word in open('words.txt'):
        words.append(word.strip())
    
    print(words)
    
