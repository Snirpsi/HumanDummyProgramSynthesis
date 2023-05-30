#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    for word in open('words.txt'):
        words.append(word.strip())
    return words

<|/ file filename=word