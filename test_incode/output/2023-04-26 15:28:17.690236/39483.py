#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    with open('words.txt', 'r') as file:
        words = [word.strip() for word in file]
    
    words.sort()
    
    print('\n'.join(words))
    
