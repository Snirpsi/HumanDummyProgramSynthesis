#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or removes words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words to remove: ")
        
    for word in words:
        if word in 