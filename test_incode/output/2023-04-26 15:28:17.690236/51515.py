#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or iterates over words. """    
    while True:
        words = input("Enter a word: ")
        if words:
            print(" ".join(words))
        else:
            break
