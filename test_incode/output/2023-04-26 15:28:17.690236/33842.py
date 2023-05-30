#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns words. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    return words
