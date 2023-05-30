#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and removes numbers. """    
    import sys
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    for word in words:
        word = word.strip()
        
        if word.isdigit():
            word = word[1:]
        
        print(word)
        
