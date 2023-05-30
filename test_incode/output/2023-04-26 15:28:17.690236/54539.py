#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words. """    
    while True:
        words = input("Enter a word: ").split()
        for word in words:
            print(word)
        
