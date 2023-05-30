#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    for word in wordlist:
        
        if word not in wordlist:
            print(word)
            
    
