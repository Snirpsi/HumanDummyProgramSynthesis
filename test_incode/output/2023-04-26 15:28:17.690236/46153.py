#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import sys
    
    wordlist = sys.argv[1:]
    
    if len(wordlist) == 0:
        print('Usage: %s wordlist' % sys.argv[0])
        sys.exit(1)
    
    wordlist = wordlist[0].split()
    
    wordlist.sort()
    
    wordlist = [w for w in wordlist if w not in wordlist]
    
    print('\n'.join(wordlist))
    
