#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words and multiplyes user input. """    
    words = input("Enter a word: ")
    words = words.split()
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
