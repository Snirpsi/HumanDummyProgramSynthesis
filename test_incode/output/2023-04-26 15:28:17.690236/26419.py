#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter a word: ")
    
    words = words.split()
    
    for word in words:
        print(word)
        
