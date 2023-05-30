#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers and enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordlist>" % sys.argv[0])
        sys.exit(1)
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist = list(enumerate(wordlist))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[0]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    
    wordlist = list(sorted(wordlist, key = lambda x : x[1]))
    
    wordlist = list(zip(wordlist[0], wordlist[1]))
    