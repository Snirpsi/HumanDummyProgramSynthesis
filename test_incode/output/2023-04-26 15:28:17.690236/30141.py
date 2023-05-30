#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    
    words = open('words.txt').read().splitlines()
    
    words = [word.strip() for word in words]
    
    words = 