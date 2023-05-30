#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or calculates numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        elif word == "add":
            print(word + " is a number 