#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and returns user input. """    
    
    words = input("Enter a word: ")
    
    words = words.split()
    
    for word in words:
        if word not in 