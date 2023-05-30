#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter a word: ")
        
    print(words)
    
