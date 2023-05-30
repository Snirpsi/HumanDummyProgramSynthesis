#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or calculates user input. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        else:
            print(word)
    
