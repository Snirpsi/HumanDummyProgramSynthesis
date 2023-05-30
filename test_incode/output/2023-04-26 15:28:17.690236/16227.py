#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and prints a list of words. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            print(word)
        else:
            print("No words found")
            
