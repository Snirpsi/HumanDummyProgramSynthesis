#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or multiplyes a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        else:
            print(word + "*", end="")
            print(word, "=", word*