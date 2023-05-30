#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and iterates over words. """    
    while True:
        word = input("Enter a word: ")
        words = word.split()
        for word in words:
            print(word)
