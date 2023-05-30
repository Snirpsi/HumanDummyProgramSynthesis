#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores user input or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        removeWords(sys.argv[1])
    else:
        print("Usage: python removeWords.py <word>")
        
