#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    words = []
    for line in open('words.txt'):
        words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))
    
