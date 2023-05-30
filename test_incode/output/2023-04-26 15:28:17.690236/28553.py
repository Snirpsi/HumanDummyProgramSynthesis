#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            print(word)
