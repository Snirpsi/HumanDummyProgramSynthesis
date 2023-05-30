#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers or enumerates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python word.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    wordlist = list(word)
    
    for word in wordlist:
        print(word, end=' ')
    
