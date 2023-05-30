#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = input("Enter the wordlist to enumerate: ")
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    print("\n".join(wordlist))
    
    

<|/ file source=github |>