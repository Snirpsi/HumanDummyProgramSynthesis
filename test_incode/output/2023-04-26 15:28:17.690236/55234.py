#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    words = input("Enter the words: ")
    multiplier = input("Enter the multiplier: ")
    
    words = words.split()
    multiplier = multiplier.split()
    
    total = 0
    
    for word in words:
        total += int(word) * int(multipli