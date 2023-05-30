#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or converts words. """    
    while True:
        word = input("Enter a word: ")
        
        # Convert word to lower case and remove punctuation
        word = word.lower().translate(None, '.,;:!?¿')
        
        # Print the word if its length is greater than 