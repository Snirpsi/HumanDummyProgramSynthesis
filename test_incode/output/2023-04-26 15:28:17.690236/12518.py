#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
