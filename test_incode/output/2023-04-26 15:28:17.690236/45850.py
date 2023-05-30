#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of words. """    
    
    words = sys.argv[1:]
    
    wordlist = list(set(words))
    
    for word in wordlist:
        print(word)
    
