#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and multiplyes all ports. """    
    
    import sys
    
    words_to_remove = sys.argv[1:]
    
    words_to_remove = set(words_to_remove)
    
    words_to_multiply = set()
    
    for word in words_to_remove:
        words_to_multiply.add(word)
    
    for word in words_to_multiply:
        word = word.lower()
        
        for port in words_to_multiply:
            word = word.replace(word, str(port