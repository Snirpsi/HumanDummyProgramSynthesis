#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or converts words. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python3 remove-numbers-or-words.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    if word.isdigit():
        print("The word '" + word + "' is not number")
        sys.exit()
    
    removeNumbers(word)
    
