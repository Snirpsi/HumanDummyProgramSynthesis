#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    words.sort()
    
    