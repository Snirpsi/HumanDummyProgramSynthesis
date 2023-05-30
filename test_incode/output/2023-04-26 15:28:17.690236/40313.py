#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and stores fruits. """    
    
    words = []
    
    # Read words from a file
    with open('words.txt', 'r') as f:
        words = [word.strip() for word in f.readlines()]
    
    # Print the words and store them in a list
    print('\n'.join(words))
    
    # Return the list of words to the webserver
    return words
    
    
