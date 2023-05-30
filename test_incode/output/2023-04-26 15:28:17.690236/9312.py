#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input or returns words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words: ")
    
    for word in words:
        print(word)
        
