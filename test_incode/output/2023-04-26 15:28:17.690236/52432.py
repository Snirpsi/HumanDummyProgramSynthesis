#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or enumerates user input. """    
    
    # Get the user input from the user
    words = get_words()
    
    # Print the words to the user
    print(words)
    
    # Print the enumerated words to the user
    for word in words:
        print(word)
        
