#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and converts words. """    
    while True:
        line = input('Enter a word: ')
        line = line.strip()
        line = line.lower()
        line = line.split()
        line = line.