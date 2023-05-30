#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import sys
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split(' ')
    
    wordlist = [word.strip() for word in wordlist]
    
    wordlist = list(set(wordlist))
    
    wordlist = [word for word in wordlist if word not in wordlist]
    
    print(' '.join(wordlist))
    
