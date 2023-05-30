#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and returns words. """    
    
    words = []
    
    for word in open('words.txt'):
        words.append(word.strip())
    
    for word in words:
        print(word)
    
