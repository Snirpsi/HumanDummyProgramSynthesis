#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or removes a list of words. """    
    
    # Get the words from the user
    words = input("Enter the words: ").split()
    
    # Remove all words from the list
    words = list(filter(lambda x: x not in words, words))
    
    # Print the new list
    print("The words 