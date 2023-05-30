#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and removes a list of words. """    
    while True:
        words = input("Enter a word: ")
        words = words.split()
        words = list(set(words))
        words.sort()
        words = [word for word in words if word not in 