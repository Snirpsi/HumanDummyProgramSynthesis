#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    for word in words:
        print(word)
    
