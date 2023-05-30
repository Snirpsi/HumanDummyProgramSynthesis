#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter a list of words: ")
    
    for word in words:
        print(word)
    
