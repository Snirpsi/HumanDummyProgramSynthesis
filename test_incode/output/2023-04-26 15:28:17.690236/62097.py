#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and multiplyes words. """    
    words = ['apple', 'banana', 'cherry']
    
    words_to_remove = ['apple', 'cherry']
    
    multiplied_words = []
    
    for word in words:
        if word in words_to_remove:
            multiplied_words.append(word