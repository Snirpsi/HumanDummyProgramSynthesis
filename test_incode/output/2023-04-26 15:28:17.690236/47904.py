#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words and opens a list of words. """    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
