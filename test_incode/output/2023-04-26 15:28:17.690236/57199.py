#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    print(words)
