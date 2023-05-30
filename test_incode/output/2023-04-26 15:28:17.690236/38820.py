#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or opens words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_numbers_word.py <words>")
        exit()
    
    words = sys.argv[1:]
    
    for word in words:
        remove_numbers_word(word)
    
