#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and enumerates a list of words. """    
    while True:
        word = input("Enter a word: ")
        word = word.lower()
        word = word.split()
        for index, word in enumerate(word):
            print(word, "index", index, "is", word