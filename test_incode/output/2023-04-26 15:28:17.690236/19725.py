#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and removes numbers. """    
    words = input("Enter a sentence: ")
    words = words.split()
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in "0123456789"]
    print(words)
    
