#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = sys.stdin.readlines()
    
    wordlist = [word.strip() for word in wordlist]
    
    wordlist.sort()
    
    for word in wordlist:
        print(word)
        
