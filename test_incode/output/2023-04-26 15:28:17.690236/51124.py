#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or adds all ports. """    
    words = []
    ports = []
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        words.append(word)
        ports.append(