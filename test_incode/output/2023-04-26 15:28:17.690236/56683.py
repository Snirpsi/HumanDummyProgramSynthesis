#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words. """    
    words = []
    with open('words.txt', 'r') as words:
        for line in words:
            words = line.split(' ')
    
    words.sort()
    
    for word in words:
        print(word)
    
