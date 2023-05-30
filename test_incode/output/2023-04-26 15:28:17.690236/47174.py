#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and adds user input. """    
    while True:
        words = input("Enter words: ")
        words = words.split()
        words.extend(