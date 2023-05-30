#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    import sys
    wordlist = sys.argv[1:]
    
    wordlist = [x for x in wordlist if x not in ['-','--']]
    
    if len(wordlist) == 0:
        print('No words given')
    else:
        print('\n'.join(wordlist))
    
