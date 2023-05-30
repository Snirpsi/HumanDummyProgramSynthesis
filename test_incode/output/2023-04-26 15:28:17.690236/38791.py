#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input and converts a list of words. """    
    
    # Remove user input
    words = input("Enter a list of words: ")
    
    # Remove punctuation
    words = words.translate(None, ".,:;!?()-_+~")
    
    # Remove empty strings
    words = words.strip()
    
    # Convert list to set
    words = set(words)
    
    # Print the result
    print(words)
    
