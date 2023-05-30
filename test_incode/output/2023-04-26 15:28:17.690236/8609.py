#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or returns user input. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Enter a word: ")
    
    print(word)
    
