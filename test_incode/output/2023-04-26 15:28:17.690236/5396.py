#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [wordlist]" % sys.argv[0])
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(filter(None, wordlist))
    
    wordlist = list(set(wordlist))
    
    wordlist = list(sorted(wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 0, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 1, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 2, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 3, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 4, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 5, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 6, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 7, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 8, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 9, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 10, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 11, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 12, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 13, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 14, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 15, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 16, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 17, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 18, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 19, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 20, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 21, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 22, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 23, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 24, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 25, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 26, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 27, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 28, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 29, wordlist))
    
    wordlist = list(filter(lambda s: len(s) > 30, wordlist))
    
    wordlist = list(