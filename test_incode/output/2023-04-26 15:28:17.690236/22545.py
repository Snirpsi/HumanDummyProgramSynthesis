#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordlist.py <words>")
        exit(1)
    
    words = sys.argv[1:]
    
    wordlist = list(set(words))
    
    wordlist.sort()
    
    print("\n".join(wordlist))
    
