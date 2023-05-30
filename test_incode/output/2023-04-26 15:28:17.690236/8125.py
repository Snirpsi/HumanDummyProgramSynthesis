#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    for line in open('words.txt'):
        line = line.strip()
        words.append(line)
    return words

<|/ file filename=word