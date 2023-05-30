#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words. """    
    words = [word.strip() for word in open('words.txt')]
    print(words)
    
