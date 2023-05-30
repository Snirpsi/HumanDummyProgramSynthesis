#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words]" % sys.argv[0])
        sys.exit(0)
    
    words = sys.argv[1:]
    
    wordlist = words.split()
    
    wordlist.sort()
    
    wordlist = [word for word in wordlist if word]
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    sys.stdout.write("\n".join(wordlist))
    
    sys.stdout.flush()
    
