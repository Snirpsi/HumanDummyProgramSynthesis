#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or prints a list of words. """    
    while True:
        print("Enter a word:")
        word = input()
        if word == "":
            break
        print("You entered", word)
        print("The word is", end=' ')
        print(word, end=' ')
        print("