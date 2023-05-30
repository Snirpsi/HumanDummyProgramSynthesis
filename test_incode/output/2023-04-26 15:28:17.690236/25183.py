#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or iterates over a list of words. """    
    
    # Get the list of words from the command line
    words = list(sys.argv[1:])
    
    # If the user wants to iterate over a list of words, then iterate over the list
    if words:
        
        # Iterate over the list of words and print each word out to the screen
        for word in words:
            print(word)
    
    # If the user wants to input a word from the command line
    elif len(words):
        
        # Print the word the user inputs to the screen
        print(words[0])
    
    # If the user wants to quit 