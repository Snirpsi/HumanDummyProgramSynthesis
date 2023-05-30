#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open the file containing the words and add them to the list
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()
    
    # Return the list of words to the client
    return words

<|/ file ext=.py |>