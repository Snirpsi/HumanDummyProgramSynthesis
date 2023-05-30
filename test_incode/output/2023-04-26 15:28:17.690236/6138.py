#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    words = []
    
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    