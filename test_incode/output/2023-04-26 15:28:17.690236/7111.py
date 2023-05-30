#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or prints a port. """    
    import sys
    if len(sys.argv) > 1:
        word = sys.argv[1]
        print(convert_word(word))
    else:
        print("Usage: python3 convert_word.py <word>")
        
