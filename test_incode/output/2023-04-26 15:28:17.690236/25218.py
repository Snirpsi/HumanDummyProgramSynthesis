#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or iterates over user input. """    
    
    # Get the user input from the user
    words = get_words()
    
    # Iterate over the user input
    for word in words:
        print(word)
    
    # Print the final 