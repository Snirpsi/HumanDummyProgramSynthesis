#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words and multiplyes a port. """    
    while True:
        words = []
        port = 1
        while True:
            word = input("Enter a word: ")
            if word == 'q':
                break
            words.append(word)
            port *= 