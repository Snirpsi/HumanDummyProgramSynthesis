#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and removes numbers. """    
    words = input("Enter a word: ")
    words = words.split()
    words = [word for word in words if word.isdigit()]
    print(words)
    
