#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and enumerates a list of words. """    
    
    words = []
    
    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    word