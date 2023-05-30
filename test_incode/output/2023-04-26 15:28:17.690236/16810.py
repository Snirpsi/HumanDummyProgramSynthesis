#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and removes a list of words. """    
    while True:
        line = input('Enter a word: ')
        if line == 'quit':
            break
        words = line.split()
        for word in words:
            if word not in 