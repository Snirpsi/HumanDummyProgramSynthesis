#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and stores a list of words. """    
    words = []
    
    for word in open('words.txt'):
        words.append(word.rstrip())
    
    words.sort()
    
    print('\n'.join(words))
    
