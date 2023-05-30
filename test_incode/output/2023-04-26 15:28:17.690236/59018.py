#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = input("Enter a comma-separated list of words: ")
    
    wordlist = wordlist.split(",")
    
    print("\n".join(wordlist))
    
