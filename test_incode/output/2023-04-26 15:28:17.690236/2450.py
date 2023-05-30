#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or multiplyes a list of words. """    
    while True:
        word = input("Enter a word: ")
        multiplier = input("Enter a multiplier: ")
        multiplier = int(multiplier)
        if word == 'quit':
            break
        elif word == 'multiply':
            multiplier = multipli