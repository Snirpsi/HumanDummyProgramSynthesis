#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or returns user input. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    print(" ".join(words))
    
