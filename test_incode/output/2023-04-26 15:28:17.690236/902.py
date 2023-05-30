#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        exit(1)
    
    word = sys.argv[1]
    
    wordlist = list(word)
    
    wordlist.sort()
    
    for word in wordlist:
        if word.lower() in wordlist:
            wordlist.remove(word)
    
    print(" ".join(wordlist))
    
