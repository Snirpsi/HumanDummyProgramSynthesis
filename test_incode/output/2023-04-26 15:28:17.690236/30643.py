#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    with open('words.txt') as words:
        for line in words:
            words.append(line.strip())
    
    words.sort()
    
    print(words)
    
