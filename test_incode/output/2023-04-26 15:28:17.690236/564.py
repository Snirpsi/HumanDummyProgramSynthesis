#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    with open('words.txt', 'w') as words:
        for line in words:
            line = line.strip()
            word