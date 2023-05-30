#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over numbers and prints a list of words. """    
    words = []
    for n in range(1, 101):
        words.append(str(n))
    print(' '.join(words))
