#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
        
        if wordlist == '-':
            wordlist = sys.stdin.readlines()
        
        wordlist = list(set(wordlist))
        
        wordlist.sort()
        
        wordlist = [word for word in wordlist if word not in ('\n', '\r')]
        
        print('\n'.join(wordlist))
    else:
        print('Usage: %s wordlist' % sys.argv[0])
        
