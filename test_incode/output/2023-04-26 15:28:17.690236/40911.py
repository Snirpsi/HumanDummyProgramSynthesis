#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns user input and opens words. """    
    
    # Get the user input
    word = input("Enter a word: ")
    
    # Open the word file
    word = open(word, "r")
    
    # Print the word
    print(word.