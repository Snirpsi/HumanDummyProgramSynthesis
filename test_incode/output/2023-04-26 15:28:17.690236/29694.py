#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds user input and stores words. """    
    words = input("Enter a word: ")
    words = words.split()
    
    words = " ".join(words)
    
    print(words)
    
