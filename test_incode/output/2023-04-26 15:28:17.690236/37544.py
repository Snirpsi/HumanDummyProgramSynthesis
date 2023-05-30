#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words and removes fruits. """    
    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        
        fruits = words[: