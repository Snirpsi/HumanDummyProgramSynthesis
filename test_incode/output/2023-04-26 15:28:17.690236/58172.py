#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    while True:
        words = [word.strip() for word in open('words.txt')]
        if len(words) == 0:
            break
        print(*words, sep='