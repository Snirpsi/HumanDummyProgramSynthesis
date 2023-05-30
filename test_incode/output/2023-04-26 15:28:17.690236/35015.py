#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1].split()
    
    wordlist = words.copy()
    
    wordlist.sort()
    
    print('\n'.join(wordlist))

<|/ file source=github |>