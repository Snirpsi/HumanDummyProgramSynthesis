#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of words. """    
    while True:
        words = input("Enter a word: ")
        words.append("")
        print(" ".join(words))
        
