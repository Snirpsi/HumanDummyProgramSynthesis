#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words. """    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        words.sort()
        print(words)
        
