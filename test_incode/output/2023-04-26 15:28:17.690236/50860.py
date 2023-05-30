#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and calculates user input. """    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        words = words[: