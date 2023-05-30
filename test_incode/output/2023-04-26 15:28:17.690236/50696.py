#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    words = words[:]
    
    words.sort()
    
    for word in words:
        print(word)
        
