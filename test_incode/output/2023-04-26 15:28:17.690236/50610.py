#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words or adds a port. """    
    import sys
    wordlist = sys.argv[1:]
    port = int(sys.argv[1])
    
    if len(wordlist) == 0:
        print("Usage: %s word1 word2 ..." % sys.argv[0])
        sys.exit()
    
    wordlist = list(wordlist)
    
    for word in wordlist:
        print(word)
    
    if port > 0:
        wordlist.pop(0)
        wordlist.insert(0,str(port))
        
    for word in wordlist:
        print(word)
    
