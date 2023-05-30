#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words. """    
    
    words = []
    
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    print('\n'.join(words))
    
