#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and stores words. """    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        print("You said: " + word)
        