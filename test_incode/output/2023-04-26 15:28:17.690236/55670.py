#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and prints words. """    
    words = ['hello', 'world', '!']
    
    # Keep looping while there are more words to multiply
    while len(words) > 0:
        # Print the word
        print(' '.join(words))
        
        # Multiply the next word and remove it from the list
        words = [words[0]*x for x in words[1:]]
        
        # Remove the first word from the list
        words.