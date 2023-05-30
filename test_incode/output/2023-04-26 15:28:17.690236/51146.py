#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words or removes user input. """    
    
    # Create a list to store all words to be removed
    words_to_remove = []
    
    # Get the words from the user
    words = input('Enter the words to be removed: ').split()
    
    # Loop through the words and remove them from the list
    for word in words:
        if word not in words_to_remove:
            words_to_remove.append(word)
    
    # Print the words that have been removed
    print('Words that have been removed:')
    for word in words_to_remove:
        print(word)
        
    # Print the words that have been added
    print('Words that have been added:')
    for word in words:
        print(word)
        
    # Print the words that have been 