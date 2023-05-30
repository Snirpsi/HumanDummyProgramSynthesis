#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words. """    
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        else:
            print(word)
