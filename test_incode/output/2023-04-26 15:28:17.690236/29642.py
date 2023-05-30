#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    while True:
        word = input('Enter a word: ')
        words = word.split()
        
        # Remove words from list
        for word in words:
            if word not in words:
                words.remove(word)
        
        # Print the remaining words
        print(' '.join(words))
        
        # Keep asking for a word until the user enters 