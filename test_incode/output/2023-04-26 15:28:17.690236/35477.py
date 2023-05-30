#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words. """    
    while True:
        words = input("Enter a word: ")
        if words:
            print(words)
        else:
            break
