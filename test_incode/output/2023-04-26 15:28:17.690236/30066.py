#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or adds user input. """    
    
    # Read user input
    word = input("Enter a word: ")
    
    # Remove word
    word = word.replace(" ", "")
    
    # Add word
    word = word + " " + input("Enter a word: ")
    
    # Print output
    print(word)
    
    # Close program
    