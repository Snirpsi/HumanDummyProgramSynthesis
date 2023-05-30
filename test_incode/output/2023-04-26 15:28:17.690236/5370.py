#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes numbers. """    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        print(word)
    
    if len(words) > 1:
        remove_numbers(words)
    
    if len(words) == 1:
        remove_numbers(words)
    
