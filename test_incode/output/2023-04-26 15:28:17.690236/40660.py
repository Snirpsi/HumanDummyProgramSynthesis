#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input and multiplyes a list of words. """    
    
    words = ['cat', 'dog', 'elephant']
    
    total = 0
    
    for word in words:
        total += int(word) * int(input('How many times would you like to 