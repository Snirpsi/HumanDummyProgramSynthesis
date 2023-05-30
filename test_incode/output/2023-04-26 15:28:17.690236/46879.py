#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        if word[0].isalpha():
            print(word)
        else:
            print(word.upper())
    
