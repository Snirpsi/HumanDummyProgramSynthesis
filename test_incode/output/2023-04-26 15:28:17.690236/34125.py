#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    
    words = []
    
    with open('words.txt', 'r') as wordfile:
        for line in wordfile:
            words.append(line.strip())
    
    words.sort()
    
    print(words)
    
