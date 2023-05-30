#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of words. """    
    words = []
    
    with open('words.txt', 'r') as wordFile:
        for line in wordFile:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    print(words)
    
