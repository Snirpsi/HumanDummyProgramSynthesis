#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and multiplyes user input. """    
    while True:
        word = input("Enter a word: ")
        multiplier = input("Enter a multiplier: ")
        multiplier = int(multiplier)
        word = word.lower()
        multiplier = int(multiplier)
        multiplier = multiplier * word
        print("The multiplied word is: ", multipli