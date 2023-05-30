#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [list of words]" % sys.argv[0])
        sys.exit(1)
    
    wordlist = sys.argv[1].split()
    
    for word in wordlist:
        word = word.strip()
        
        if word not in wordlist:
            print("%s not in %s" % (word, wordlist))
            sys.exit(1)
    
    print("Removed %s from %s" % (len(wordlist), wordlist))
    sys.exit(0)

<|/ file source=github |>