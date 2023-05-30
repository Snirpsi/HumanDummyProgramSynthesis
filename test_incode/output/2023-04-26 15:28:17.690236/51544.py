#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 words_to_words.py <word>")
        exit(1)
    
    word = sys.argv[1]
    
    word