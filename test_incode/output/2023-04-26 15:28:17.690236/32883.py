#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s word" % sys.argv[0])
        sys.exit(1)
    
    wordlist = sys.argv[1].split()
    
    for word in wordlist:
        word = word.strip()
        
        if word == '':
            continue
        
        print("%s %s" % (word, word