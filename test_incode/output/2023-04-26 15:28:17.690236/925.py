#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and iterates over user input. """    
    while True:
        words = input("Enter a word: ")
        for word in words.split():
            print(word)
