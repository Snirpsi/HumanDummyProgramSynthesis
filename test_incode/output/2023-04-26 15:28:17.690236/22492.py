#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and returns words. """    
    while True:
        word = input("Enter a word: ")
        if word == '':
            print("You did not enter a word.")
        else:
            print(word)
