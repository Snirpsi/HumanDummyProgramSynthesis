#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input and prints a list of words. """    
    while True:
        line = input('Enter a word: ')
        line = line.strip()
        line = line.lower()
        line = line.split()
        line = line.