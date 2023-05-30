#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and adds user input. """    
    
    words = []
    
    # Read user input from the terminal
    words.append(input("Enter a word: "))
    
    # Iterate over the list of words and print the word
    for word in words:
        print(word)
        
