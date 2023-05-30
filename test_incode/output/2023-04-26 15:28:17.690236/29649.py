#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words or calculates numbers. """    
    while True:
        word = input("Enter a word: ")
        if word == "exit":
            break
        else:
            print(word)
            