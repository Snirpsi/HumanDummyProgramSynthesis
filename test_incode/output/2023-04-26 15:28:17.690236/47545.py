#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and iterates over a list of words. """    
    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    # Remove all numbers from the list
    words = [word for word in words if word.isdigit()]
    
    # Iterate over each word
    for word in words:
        print(word)
        
    # Stop the server when all words have been iterated
    