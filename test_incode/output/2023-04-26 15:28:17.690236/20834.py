#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    import sys
    
    wordlist = sys.argv[1:]
    
    removed = []
    for word in wordlist:
        if word not in removed:
            removed.append(word)
    
    print('\n'.join(removed))
    
