#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input and removes a list of words. """    
    
    # Get the user input
    word = input("Enter a word: ")
    
    # Remove word
    word = word.split()
    word = " ".join(word)
    
    # Print the result
    print("The word is ", word)
    
    # Close the program
    exit()
    
