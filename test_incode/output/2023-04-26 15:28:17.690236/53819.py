#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = sys.stdin.read().split()
    
    wordlist.sort()
    
    wordlist = [wordlist[i] for i in range(1, len(wordlist))]
    
    sys.stdout.write('\n'.join(wordlist))
    
