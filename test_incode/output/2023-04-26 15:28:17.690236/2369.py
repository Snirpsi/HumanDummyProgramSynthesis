#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and adds user input. """    
    words = input("Enter a sentence: ").split()
    
    # Add user input to the list
    words.extend(